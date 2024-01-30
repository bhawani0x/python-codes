# User function Template for python3

class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        max_sum = 0
        current_sum = 0

        for num in arr:
            current_sum += num
            if current_sum == 0:
                current_sum -= num
            max_sum = max(max_sum, current_sum)

        return max_sum


import math


def main():
    n = 5

    arr = [1, 2, 3, -2, 5]

    ob = Solution()

    print(ob.maxSubArraySum(arr, n))


if __name__ == "__main__":
    main()
# } Driver Code Ends
