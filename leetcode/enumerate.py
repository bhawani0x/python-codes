# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
#
# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
#
# print("Return type:", type(obj1))
# print(list(enumerate(l1)))
# print(set(obj2))
#
# # changing start index to 2 from 0
# print((enumerate(s1)))


a = [1, 2, 3, 4, 5, 6, 7, 8]
a = "bhawnai singh"
a = enumerate(a)

for index, value in a:
    print(index, "  ", value)
