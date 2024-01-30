# User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        li = []
        current = next = small = 0

        for i in range(len(S) - 1):
            current = S[i]
            next = S[i + 1]
            if current <= next:
                small = current
                li.append(small)

            if current > next:
                small = next


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    S = "149811"
    K = 3

    obj = Solution()

    ans = obj.removeKdigits(S, K)

    print(ans)

# } Driver Code Ends
