class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -(2 ** 31), 2 ** 31 - 1

        is_negative = x < 0
        x = abs(x)

        reversed_x = int(str(x)[::-1])
        if is_negative:
            reversed_x *= -1

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x


s = Solution()
print(s.reverse(-2143847412))
