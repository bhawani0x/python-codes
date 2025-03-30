# next greater permutation
def reverse_arr(arr):
	for i in range(len(arr) // 2):
		arr[i], arr[-1 - i] = arr[-1 - i], arr[i]
	return arr

def next_permutation(arr:list)-> list:
	p_point = -1
	for i in range(len(arr) - 2, -1, -1):
		if arr[i] < arr[i + 1]:
			p_point = i
			break

	if p_point == -1:
		print("no P_point")
		reverse_arr(arr)

	# find the lowest  value and swap with p_point and then sort the remaining value from the p_point

	for i in range(len(arr)-1, p_point, -1):
		if arr[i] > arr[p_point]:
			arr[i], arr[p_point] = arr[p_point], arr[i]
			break

	arr[p_point+1:] =  reverse_arr(arr[p_point+1:])
	return arr

arr = [3, 4, 5, 3, 1, 5, 4] # ans is [3,4,5,3,1,4,5]
print(next_permutation(arr.copy()))
