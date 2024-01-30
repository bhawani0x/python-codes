if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5]
    leftSum = 0
    for i in range(len(arr)):
        leftSum += arr[i]
        rightSum = 0
        for j in range(i + 1, len(arr)):
            rightSum += arr[j]
        if leftSum == rightSum:
            split = i
            print(leftSum, rightSum)

    print([arr[i] for i in range(len(arr)) if i != split + 1])
    print([arr[i] for i in range(len(arr)) if i == split + 1])
