if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    sum_ = 18
    subarrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j+1]
            subarrays.append(subarray)
    print(subarrays)

    # for i in subarrays:
    #     arr_sum = 0
    #     if len(i) == 4:
    #         for j in i:
    #             arr_sum += j
    #         if arr_sum == sum_:
    #             print(True)

    for i in subarrays:
        arr_sum = 0
        if len(i) == 4:
            if sum(i) == sum_:
                print(True)


    print(any(sum(i) == sum_ for i in subarrays if len(i) == 4))
