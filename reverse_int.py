class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2 ** 31 - 1
        min = (-2) ** 31
        is_negative = False
        if x < 0:
            is_negative = True
        if x < min or x > max:
            return 0
        x = str(x)[::-1]
        if is_negative:
            x = "-" + x
        return int(x)


a = Solution()
print(a.reverse(1534236469))
