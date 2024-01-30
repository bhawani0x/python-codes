if __name__ == "__main__":
    nums = [0,0,0]
    nums.sort()
    subarray = []
    if len(nums) == 3 and sum(nums) == 0:
        print(nums)
    else:
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    sub = [nums[i], nums[left], nums[right]]
                    subarray.append(sub)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        print(subarray)
    # return (subarray)