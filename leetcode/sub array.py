def longest_subarray_with_sum_divisible_by_k(arr, k):
    n = len(arr)

    # Create a dictionary to store the remainder and its index
    remainder_index = {0: -1}

    # Initialize variables
    current_sum = 0
    max_length = 0

    for i in range(n):
        current_sum += arr[i]

        # Calculate the remainder
        remainder = current_sum % k

        # If the remainder is negative, add k to make it positive
        if remainder < 0:
            remainder += k

        # If the remainder is already in the dictionary, update max_length
        if remainder in remainder_index:
            max_length = max(max_length, i - remainder_index[remainder])

        # If the remainder is not in the dictionary, add it with the current index
        if remainder not in remainder_index:
            remainder_index[remainder] = i

    return max_length


# Example usage:

arr = [2, 7, 6, 1, 4, 5]
k = 3
result = longest_subarray_with_sum_divisible_by_k(arr, k)
print("Length of the longest subarray with sum divisible by", k, "is:", result)
