"""
Simple unit tests for Task 1 sorting functions.
Run: python code/task1_tests.py
"""

from task1_sorting import sort_dicts_by_key
from task1_sorting_manual import sort_dicts_by_key_manual

def run_tests():
    data = [
        {"id": "a", "score": 10},
        {"id": "b"},
        {"id": "c", "score": 5},
        {"id": "d", "score": 10},
    ]

    expected_by_score = [
        {"id": "b"},
        {"id": "c", "score": 5},
        {"id": "a", "score": 10},
        {"id": "d", "score": 10},
    ]

    s1 = sort_dicts_by_key(data, "score")
    s2 = sort_dicts_by_key_manual(data, "score")

    print("AI-suggested sorted:", s1)
    print("Manual sorted:", s2)

    assert [d.get("id") for d in s1] == [d.get("id") for d in expected_by_score], "AI-suggested failed"
    assert [d.get("id") for d in s2] == [d.get("id") for d in expected_by_score], "Manual failed"

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
