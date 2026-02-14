"""
Advanced example showing data query optimization with Agent Memory
"""

import sys
import os
from typing import List, Dict, Any

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agent_memory import MemoryStore, AgentMemoryConfig
from src.utils.helpers import summarize_memories


class OptimizedAgentQuery:
    """
    Demonstrates optimized query patterns for agent memory
    """
    
    def __init__(self):
        self.config = AgentMemoryConfig()
        self.memory_store = MemoryStore(self.config)
    
    def batch_add_memories(self, memories: List[Dict[str, Any]]) -> None:
        """
        Add multiple memories efficiently
        
        Args:
            memories: List of memory dictionaries with content and metadata
        """
        print(f"Adding {len(memories)} memories in batch...")
        for mem in memories:
            self.memory_store.add_memory(
                content=mem["content"],
                metadata=mem.get("metadata", {})
            )
        print(f"✓ Successfully added {len(memories)} memories")
    
    def smart_query(
        self,
        query: str,
        context: Dict[str, Any] = None,
        n_results: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Perform a smart query with context awareness
        
        Args:
            query: Query string
            context: Optional context for filtering
            n_results: Number of results to return
            
        Returns:
            List of relevant memories
        """
        print(f"\nExecuting smart query: '{query}'")
        
        # Build filter from context
        filter_metadata = None
        if context:
            filter_metadata = context
            print(f"  Context filters: {filter_metadata}")
        
        # Query memories
        results = self.memory_store.query_memories(
            query=query,
            n_results=n_results,
            filter_metadata=filter_metadata
        )
        
        print(f"  Found {len(results)} relevant memories")
        return results
    
    def get_contextual_history(
        self,
        user_id: str,
        category: str = None
    ) -> List[Dict[str, Any]]:
        """
        Get contextual history for a specific user
        
        Args:
            user_id: User identifier
            category: Optional category filter
            
        Returns:
            List of user's memories
        """
        all_memories = self.memory_store.get_all_memories()
        
        # Filter by user
        user_memories = [
            m for m in all_memories
            if m['metadata'].get('user_id') == user_id
        ]
        
        # Filter by category if provided
        if category:
            user_memories = [
                m for m in user_memories
                if m['metadata'].get('category') == category
            ]
        
        return user_memories


def main():
    """
    Demonstrate optimized query patterns
    """
    print("=== Agent Memory - Optimized Queries Example ===\n")
    
    agent = OptimizedAgentQuery()
    
    # Sample data representing customer interactions
    customer_data = [
        {
            "content": "Cliente perguntou sobre investimentos em CDB com liquidez diária",
            "metadata": {"user_id": "client_001", "category": "investments", "product": "CDB"}
        },
        {
            "content": "Interesse em financiamento imobiliário para primeira casa",
            "metadata": {"user_id": "client_002", "category": "loans", "product": "financing"}
        },
        {
            "content": "Solicitação de aumento de limite do cartão de crédito",
            "metadata": {"user_id": "client_001", "category": "credit_card", "product": "credit_card"}
        },
        {
            "content": "Dúvidas sobre previdência privada e PGBL",
            "metadata": {"user_id": "client_003", "category": "investments", "product": "pension"}
        },
        {
            "content": "Cliente quer transferir investimentos de outro banco",
            "metadata": {"user_id": "client_001", "category": "investments", "product": "transfer"}
        },
        {
            "content": "Consulta sobre seguro residencial com cobertura ampla",
            "metadata": {"user_id": "client_004", "category": "insurance", "product": "home_insurance"}
        }
    ]
    
    # Batch add memories
    agent.batch_add_memories(customer_data)
    
    # Demonstrate smart queries
    print("\n=== Smart Query Examples ===")
    
    # Query 1: General investment query
    results = agent.smart_query(
        query="investimentos de longo prazo",
        n_results=3
    )
    
    for i, result in enumerate(results, 1):
        print(f"\n  {i}. {result['content']}")
        print(f"     User: {result['metadata'].get('user_id')}")
        if 'relevance' in result:
            print(f"     Relevance: {result['relevance']:.2f}")
    
    # Query 2: Contextual query for specific user
    print("\n=== Contextual History for client_001 ===")
    user_history = agent.get_contextual_history(user_id="client_001")
    
    print(f"Found {len(user_history)} interactions for client_001:")
    for i, mem in enumerate(user_history, 1):
        print(f"\n  {i}. {mem['content']}")
        print(f"     Category: {mem['metadata'].get('category')}")
        print(f"     Product: {mem['metadata'].get('product')}")
    
    # Query 3: Category-specific query
    print("\n=== Investment-related memories for client_001 ===")
    investment_history = agent.get_contextual_history(
        user_id="client_001",
        category="investments"
    )
    
    for i, mem in enumerate(investment_history, 1):
        print(f"\n  {i}. {mem['content']}")
    
    # Summary statistics
    print("\n=== Memory Statistics ===")
    all_memories = agent.memory_store.get_all_memories()
    summary = summarize_memories(all_memories)
    
    print(f"Total memories: {summary['total_count']}")
    if summary['date_range']['earliest']:
        print(f"Earliest: {summary['date_range']['earliest']}")
        print(f"Latest: {summary['date_range']['latest']}")
    
    print("\n=== Example Complete ===")


if __name__ == "__main__":
    main()
