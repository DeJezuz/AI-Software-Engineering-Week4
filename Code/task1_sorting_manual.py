"""
Manual sorting implementation (educational)
File: code/task1_sorting_manual.py
"""

from typing import List, Dict, Any

def sort_dicts_by_key_manual(dicts: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Manual implementation: stable sort using list of tuples then reconstruct.
    Demonstrates the underlying logic of sorting with stability.
    """
    # Build list of tuples: (missing_flag, value, original_index, dict)
    # missing_flag ensures missing values go after present values when reverse=False
    indexed = []
    for i, d in enumerate(dicts):
        val = d.get(key, None)
        missing = val is None
        indexed.append((missing, val, i, d))

    # Sort by (missing_flag, val, original_index)
    indexed.sort(key=lambda t: (t[0], t[1], t[2]), reverse=reverse)

    # Reconstruct sorted dictionaries
    return [t[3] for t in indexed]


if __name__ == "__main__":
    demo = [
        {"id": 1, "priority": 5},
        {"id": 2},
        {"id": 3, "priority": 1},
        {"id": 4, "priority": 3},
    ]
    print("Manual sorted:", sort_dicts_by_key_manual(demo, "priority"))
