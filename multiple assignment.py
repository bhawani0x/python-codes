# a = b = c = d = 55
# b= 10
# print(id(a), id(b), id(c), id(d ))
#
# name = "Bhawani Singh"
# print(name[slice(3,-1)])
#

# def fun(*args, **kwargs):
#     print(args)
#     print(type(args))
#     print(kwargs)
#     print(type(kwargs))
#
#
# fun(121, 212, 12321, a=21, b=2, c=3, d=3)

#
# import random
#
# a = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a)

def fun(val):
    return val * val


li = [2, 4, 23, 13, 21, 123, 1]
a = list(map(fun, li))
print(a)
