# Input: arr[] = {-2, -1, 3, -4, 5}, K = 2
# Output: YES

if __name__ == '__main__':
    arr = [-2, -1, 3, -4, 5]
    sunarrays = []
    k = 12
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sunarray = arr[i:j + 1]
            sunarrays.append(sunarray)
    print(sunarrays)

    for i in range(len(sunarrays)):
        if len(sunarrays[i]) != 1:
            prodict = 1
            for j in range(len(sunarrays[i])):
                prodict *= sunarrays[i][j]
            print(prodict, end=", ")
