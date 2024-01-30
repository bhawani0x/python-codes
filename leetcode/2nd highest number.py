a = [1, 3, 2, 53, 4, 3, 3, 2, 21, 3, 323]

hi = float(-999999999)
hi2 = float(-99999999)

for i in a:
    if i > hi:
        hi2 = hi
        hi = i
print(hi2)
