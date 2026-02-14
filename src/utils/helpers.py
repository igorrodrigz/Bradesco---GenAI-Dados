"""
Helper functions for memory formatting and processing
"""

from typing import Dict, Any, List
from datetime import datetime


def format_memory(memory: Dict[str, Any]) -> str:
    """
    Format a memory for display
    
    Args:
        memory: Memory dictionary
        
    Returns:
        Formatted string representation
    """
    output = f"Memory ID: {memory.get('id', 'N/A')}\n"
    output += f"Content: {memory.get('content', 'N/A')}\n"
    
    if 'metadata' in memory:
        output += "Metadata:\n"
        for key, value in memory['metadata'].items():
            output += f"  {key}: {value}\n"
    
    if 'relevance' in memory:
        output += f"Relevance: {memory['relevance']:.2f}\n"
    
    return output


def calculate_relevance(distance: float) -> float:
    """
    Calculate relevance score from distance
    
    Args:
        distance: Distance value from vector search
        
    Returns:
        Relevance score (0-1)
    """
    return max(0.0, min(1.0, 1.0 - distance))


def filter_by_date_range(
    memories: List[Dict[str, Any]],
    start_date: datetime,
    end_date: datetime
) -> List[Dict[str, Any]]:
    """
    Filter memories by date range
    
    Args:
        memories: List of memory dictionaries
        start_date: Start date
        end_date: End date
        
    Returns:
        Filtered list of memories
    """
    filtered = []
    for memory in memories:
        if 'metadata' in memory and 'timestamp' in memory['metadata']:
            timestamp = datetime.fromisoformat(memory['metadata']['timestamp'])
            if start_date <= timestamp <= end_date:
                filtered.append(memory)
    return filtered


def summarize_memories(memories: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate summary statistics for a list of memories
    
    Args:
        memories: List of memory dictionaries
        
    Returns:
        Dictionary with summary statistics
    """
    return {
        "total_count": len(memories),
        "avg_relevance": sum(m.get('relevance', 0) for m in memories) / len(memories) if memories else 0,
        "date_range": {
            "earliest": min(
                (m['metadata']['timestamp'] for m in memories if 'metadata' in m and 'timestamp' in m['metadata']),
                default=None
            ),
            "latest": max(
                (m['metadata']['timestamp'] for m in memories if 'metadata' in m and 'timestamp' in m['metadata']),
                default=None
            )
        }
    }
