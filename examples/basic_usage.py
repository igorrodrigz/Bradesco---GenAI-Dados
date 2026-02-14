"""
Basic example of using the Agent Memory system
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agent_memory import MemoryStore, AgentMemoryConfig
from src.utils.helpers import format_memory


def main():
    """
    Demonstrate basic usage of the Agent Memory system
    """
    print("=== Agent Memory System - Basic Example ===\n")
    
    # Initialize configuration
    config = AgentMemoryConfig()
    print(f"Configuration loaded:")
    print(f"  - Collection: {config.chroma_collection_name}")
    print(f"  - Max size: {config.max_memory_size}")
    print(f"  - Relevance threshold: {config.memory_relevance_threshold}\n")
    
    # Initialize memory store
    print("Initializing Memory Store...")
    memory_store = MemoryStore(config)
    
    # Add some sample memories
    print("\nAdding sample memories...")
    
    memories_to_add = [
        {
            "content": "Usuário solicitou informações sobre produtos bancários",
            "metadata": {"category": "banking", "user_id": "user123"}
        },
        {
            "content": "Cliente interessado em investimentos de renda fixa",
            "metadata": {"category": "investments", "user_id": "user123"}
        },
        {
            "content": "Consulta sobre taxas de empréstimo pessoal",
            "metadata": {"category": "loans", "user_id": "user456"}
        },
        {
            "content": "Dúvidas sobre abertura de conta corrente",
            "metadata": {"category": "banking", "user_id": "user789"}
        }
    ]
    
    for mem in memories_to_add:
        memory_id = memory_store.add_memory(
            content=mem["content"],
            metadata=mem["metadata"]
        )
        print(f"  Added: {mem['content'][:50]}... [ID: {memory_id[:8]}...]")
    
    # Count memories
    total = memory_store.count_memories()
    print(f"\nTotal memories in store: {total}")
    
    # Query memories
    print("\n=== Querying Memories ===")
    
    queries = [
        "investimentos e aplicações financeiras",
        "abertura de conta",
        "empréstimo"
    ]
    
    for query in queries:
        print(f"\nQuery: '{query}'")
        results = memory_store.query_memories(query, n_results=2)
        
        if results:
            print(f"Found {len(results)} relevant memories:")
            for i, result in enumerate(results, 1):
                print(f"\n  Result {i}:")
                print(f"    Content: {result['content']}")
                print(f"    Category: {result['metadata'].get('category', 'N/A')}")
                if 'relevance' in result:
                    print(f"    Relevance: {result['relevance']:.2f}")
        else:
            print("  No relevant memories found")
    
    # Get all memories
    print("\n=== All Memories ===")
    all_memories = memory_store.get_all_memories()
    print(f"Total: {len(all_memories)} memories")
    for i, mem in enumerate(all_memories, 1):
        print(f"\n{i}. {mem['content']}")
        print(f"   Category: {mem['metadata'].get('category', 'N/A')}")
    
    print("\n=== Example Complete ===")


if __name__ == "__main__":
    main()
