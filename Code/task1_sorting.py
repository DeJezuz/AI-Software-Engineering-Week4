"""
AI-suggested sorting util
File: code/task1_sorting.py
"""

from typing import List, Dict, Any

def sort_dicts_by_key(dicts: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sort a list of dictionaries by a given key using Python's built-in sorted.
    Returns a new list. If a dict is missing the key it is treated as None.

    Example:
        items = [{'a': 3}, {'a': 1}, {'b': 2}]
        sort_dicts_by_key(items, 'a') -> [{'b': 2}, {'a': 1}, {'a': 3}]
    """
    # Use .get to safely handle missing keys; None will sort before numbers/strings if not reversed.
    return sorted(dicts, key=lambda d: d.get(key, None), reverse=reverse)


if __name__ == "__main__":
    # Small demo
    demo = [
        {"id": 1, "priority": 5},
        {"id": 2},
        {"id": 3, "priority": 1},
        {"id": 4, "priority": 3},
    ]
    print("Original:", demo)
    print("Sorted by priority:", sort_dicts_by_key(demo, "priority"))
