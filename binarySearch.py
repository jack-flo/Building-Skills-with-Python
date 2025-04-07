# Binary search a sorted sequence
sequence = [1, 2, 3, 4, 5]
target = 5

low, high = 0, len(sequence)
midpoint = 0

while (low + 1) < high and sequence[midpoint] != target:
    midpoint = (low + high) // 2
    if target < sequence[midpoint]:
        high = midpoint
    elif target > sequence[midpoint]:
        low = midpoint

print(f"The target's index is {midpoint}")
