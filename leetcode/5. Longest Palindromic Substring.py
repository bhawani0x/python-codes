class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        temp = []
        for index, value in enumerate(s):
            if value not in temp:
                temp.append(value)
            else:
                max_len = max(max_len, len(temp))



s = Solution()
s.longestPalindrome("abcdab")
