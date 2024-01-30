# User function Template for python3


class Solution:
    def missingNumber(self, array, n):
        s = sum(array)
        original_sum = (n * (n + 1)) * 0.5
        return int(original_sum - s)

        # code here

    # {
    # Driver Code Starts
    # Initial Template for Python 3


n = 5
a = [1, 2, 3, 5]
s = Solution().missingNumber(a, n)
print(s)
# } Driver Code Ends
