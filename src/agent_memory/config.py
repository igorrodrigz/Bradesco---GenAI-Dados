"""
Configuration module for Agent Memory system
"""

import os
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AgentMemoryConfig(BaseModel):
    """Configuration for the Agent Memory system"""
    
    openai_api_key: str = Field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY", ""),
        description="OpenAI API key for embeddings"
    )
    
    chroma_persist_directory: str = Field(
        default_factory=lambda: os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db"),
        description="Directory to persist ChromaDB data"
    )
    
    chroma_collection_name: str = Field(
        default_factory=lambda: os.getenv("CHROMA_COLLECTION_NAME", "agent_memory"),
        description="Name of the ChromaDB collection"
    )
    
    max_memory_size: int = Field(
        default_factory=lambda: int(os.getenv("MAX_MEMORY_SIZE", "100")),
        description="Maximum number of memories to store"
    )
    
    memory_relevance_threshold: float = Field(
        default_factory=lambda: float(os.getenv("MEMORY_RELEVANCE_THRESHOLD", "0.7")),
        description="Minimum relevance score for memory retrieval"
    )
    
    class Config:
        """Pydantic configuration"""
        arbitrary_types_allowed = True


def get_config() -> AgentMemoryConfig:
    """Get the current configuration"""
    return AgentMemoryConfig()
