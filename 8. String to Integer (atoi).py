class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        num = ""
        for index, value in enumerate(s):

            if value.isalpha() and index == 0:
                return 0
            if value == '-':
                num += value
            if value.isnumeric():
                num += value

        print(int(num))


s = Solution()
s.myAtoi("helklo -4193 with words")
