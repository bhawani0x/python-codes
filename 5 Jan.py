vert = [
    [[5.25, 2.51, 0], [5.25, 2.51, 1], [5.13, 2.51, 0], [5.13, 2.51, 1]],
    [[5.13, 2.51, 0], [5.13, 2.51, 1], [5.13, 3.82, 0], [5.13, 3.82, 1]],
    [[5.13, 3.82, 0], [5.13, 3.82, 1], [5.12, 3.83, 0], [5.12, 3.83, 1]],
    [[5.12, 3.83, 0], [5.12, 3.83, 1], [4.73, 3.83, 0], [4.73, 3.83, 1]],
    [[4.73, 3.83, 0], [4.73, 3.83, 1], [4.73, 3.95, 0], [4.73, 3.95, 1]],
    [[4.73, 3.95, 0], [4.73, 3.95, 1], [5.24, 3.95, 0], [5.24, 3.95, 1]],
    [[5.24, 3.95, 0], [5.24, 3.95, 1], [5.25, 3.94, 0], [5.25, 3.94, 1]],
    [[5.25, 3.94, 0], [5.25, 3.94, 1], [5.25, 2.51, 0], [5.25, 2.51, 1]],
]
two_dimentional_array = []
for i in vert:
    two_dimentional_array.append([i[0][0], i[0][1]])
    # two_dimentional_array.append([i[0][1]])

# print(two_dimentional_array[0][1])
# for j in two_dimentional_array:
# print(j.index(j[1]))

print(two_dimentional_array)

for i in range(len(two_dimentional_array) - 1):
    x1 = two_dimentional_array[i][0]
    x2 = two_dimentional_array[i - 1][0]
    y1 = two_dimentional_array[i][1]
    y2 = two_dimentional_array[i - 1][1]
    if y1 == y2:
        print("Y same",(x1,y1),(x2,y2),"diff.", abs(x1-x2))
        x_difference = abs(x1-x2)
    if x1 == x2:
        print("X same", (x1, y1), (x2, y2), "diff.", abs(y1 - y2))
        y_difference = abs(y1 - y2)
    # if y1 != y2:
    #     print("Y not same",(x1,y1),(x2,y2))
    # if x1 != x2:
    #     print("X not same",(x1,y1),(x2,y2))
    # if y1 != y2:
    #     print(x1,x2,y1,y2)