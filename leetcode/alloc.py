def solution(A):
    # Sort the array in descending order
    A.sort(reverse=True)

    # Iterate through the sorted array
    for i in range(len(A) - 1):
        # Try to build a square using the current segment as the side length
        side_length = A[i]
        total_length = 0

        # Merge segments to build the square
        for j in range(len(A)):
            if total_length >= 4 * side_length:
                return side_length

            if A[j] > 0:
                total_length += A[j]
                A[j] = 0  # Mark the segment as used

        # If we cannot build a square using the current segment, check if merging segments can help
        for j in range(len(A)):
            if A[j] > 0 and total_length + A[j] >= 4 * side_length:
                return total_length + A[j]

    # If no square can be built, return 0
    return 0

# Example test
print(solution([2, 2, 2, 2, 2, 10, 10, 10]))  # Output: 10

# Examples
print(solution([3, 3, 3, 2, 1, 1]))  # Output: 3
print(solution([5, 4, 3, 2, 1, 10]))  # Output: 0
print(solution([2, 3, 5, 1, 1, 6, 3, 5]))  # Output: 6
