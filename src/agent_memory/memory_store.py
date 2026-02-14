"""
Memory Store implementation using ChromaDB for vector storage
"""

from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime
import chromadb
from chromadb.config import Settings
from langchain.embeddings import OpenAIEmbeddings
from .config import AgentMemoryConfig


class MemoryStore:
    """
    Memory storage system for AI agents using ChromaDB.
    Provides efficient storage and retrieval of agent interactions.
    """
    
    def __init__(self, config: Optional[AgentMemoryConfig] = None):
        """
        Initialize the Memory Store
        
        Args:
            config: Configuration object. If None, uses default config.
        """
        self.config = config or AgentMemoryConfig()
        
        # Initialize ChromaDB client
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=self.config.chroma_persist_directory
        ))
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.config.chroma_collection_name
        )
        
        # Initialize embeddings
        if self.config.openai_api_key:
            self.embeddings = OpenAIEmbeddings(
                openai_api_key=self.config.openai_api_key
            )
        else:
            self.embeddings = None
    
    def add_memory(
        self,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        memory_id: Optional[str] = None
    ) -> str:
        """
        Add a new memory to the store
        
        Args:
            content: The content of the memory
            metadata: Optional metadata associated with the memory
            memory_id: Optional custom ID. If None, generates a UUID.
            
        Returns:
            The ID of the stored memory
        """
        if memory_id is None:
            memory_id = str(uuid.uuid4())
        
        # Prepare metadata
        if metadata is None:
            metadata = {}
        metadata["timestamp"] = datetime.now().isoformat()
        
        # Add to collection
        self.collection.add(
            documents=[content],
            metadatas=[metadata],
            ids=[memory_id]
        )
        
        return memory_id
    
    def query_memories(
        self,
        query: str,
        n_results: int = 5,
        filter_metadata: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Query memories based on semantic similarity
        
        Args:
            query: The query string
            n_results: Number of results to return
            filter_metadata: Optional metadata filters
            
        Returns:
            List of relevant memories with their metadata
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=filter_metadata
        )
        
        # Format results
        memories = []
        if results["documents"] and results["documents"][0]:
            for i, doc in enumerate(results["documents"][0]):
                memory = {
                    "id": results["ids"][0][i],
                    "content": doc,
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i] if "distances" in results else None
                }
                
                # Apply relevance threshold
                if memory["distance"] is not None:
                    relevance = 1 - memory["distance"]
                    if relevance >= self.config.memory_relevance_threshold:
                        memory["relevance"] = relevance
                        memories.append(memory)
                else:
                    memories.append(memory)
        
        return memories
    
    def get_memory(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific memory by ID
        
        Args:
            memory_id: The ID of the memory
            
        Returns:
            The memory dict or None if not found
        """
        results = self.collection.get(
            ids=[memory_id]
        )
        
        if results["documents"]:
            return {
                "id": memory_id,
                "content": results["documents"][0],
                "metadata": results["metadatas"][0]
            }
        return None
    
    def delete_memory(self, memory_id: str) -> bool:
        """
        Delete a memory from the store
        
        Args:
            memory_id: The ID of the memory to delete
            
        Returns:
            True if deleted, False if not found
        """
        try:
            self.collection.delete(ids=[memory_id])
            return True
        except Exception:
            return False
    
    def get_all_memories(self) -> List[Dict[str, Any]]:
        """
        Get all memories from the store
        
        Returns:
            List of all memories
        """
        results = self.collection.get()
        
        memories = []
        if results["documents"]:
            for i, doc in enumerate(results["documents"]):
                memories.append({
                    "id": results["ids"][i],
                    "content": doc,
                    "metadata": results["metadatas"][i]
                })
        
        return memories
    
    def clear_all_memories(self) -> None:
        """Clear all memories from the store"""
        # Delete and recreate collection
        self.client.delete_collection(name=self.config.chroma_collection_name)
        self.collection = self.client.get_or_create_collection(
            name=self.config.chroma_collection_name
        )
    
    def count_memories(self) -> int:
        """
        Get the count of memories in the store
        
        Returns:
            Number of memories
        """
        return self.collection.count()
