test_list = [1, 3, 4, 4, 2, 3]
group = {}
for ele in test_list:
    if ele in group:
        group[ele].append(ele)
    else:
        group[ele] = [ele]
print(group.values())

