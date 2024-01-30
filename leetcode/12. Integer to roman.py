class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        number = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        a = zip(values, symbols)
        print(list(a))
        for value, symbol in zip(values, symbols):
            while num >= value:
                num -= value
                number += symbol
        return number


s = Solution()
print(s.intToRoman(3))

print(3%10)