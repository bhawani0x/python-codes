# this will not work if n >100 or fact > int value

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# n = 120
#
# fact = factorial(n)
# trailing_zeros = 0
#
# while (fact % 10 == 0):
#     fact = fact // 10
#     trailing_zeros += 1
#
# print(trailing_zeros)

n = 100
zero = 0
i = 1
while (n >= 5 ** i):
    zero += n // 5 ** i
    i+=1
print(zero)

###### Formula
# n//5+n//125....where n>=5^x  and x is real number
