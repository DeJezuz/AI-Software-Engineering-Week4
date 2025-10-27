# Task 1: AI-Powered Code Completion
# Author: Gervásio MAGUL
# Description: Compare Copilot-generated and manual sorting functions for a list of dictionaries.

# Sample data
data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 82}
]

# --- Copilot-Suggested Version ---
def sort_dicts_by_key(data, key):
    """
    Sorts a list of dictionaries by a given key using Python's built-in sorted().
    Efficient and concise.
    """
    return sorted(data, key=lambda x: x[key])

# --- Manual Implementation ---
def sort_dicts_by_key_manual(data, key):
    """
    Sorts a list of dictionaries by a given key using bubble sort.
    Less efficient, but demonstrates algorithmic understanding.
    """
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# --- Execution ---
print("Original:", data)
print("Copilot Sorted:", sort_dicts_by_key(data, "score"))
print("Manual Sorted:", sort_dicts_by_key_manual(data.copy(), "score"))
