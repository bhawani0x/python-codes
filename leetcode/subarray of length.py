if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4

    subarrays = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j + 1]
            if len(subarray) == k:
                subarrays.append(subarray)

    print(subarrays)

