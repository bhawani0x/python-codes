if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    subarrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j + 1]
            subarrays.append(subarray)
            # print([arr[i], arr[j+1]])
    print(subarrays)
