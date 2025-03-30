# rotate an array to left side by D
# these are multiple methods are there lets go through one by one


# method 1: store data in tmp and move array to left and replace the last element with it.
def method_1(arr: list, d: int) -> list:
	for i in range(d):
		tmp = arr[0]
		arr[:-1] = arr[1:]
		arr[-1] = tmp
	return arr


# method 2: store d element in a tmp and shift d element in left and replace the last d element
def method_2(arr: list, d: int) -> list:
	tmp = arr[:d]
	arr = arr[d:]
	arr.extend(tmp)
	return arr


# method 3: juggling method, reverse first d array and remaining array and then reverse all the array
def reverse_arr(arr):
	for i in range(len(arr) // 2):
		arr[i], arr[-1-i] = arr[-1-i], arr[i]
	return arr


def method_3(arr: list, d: int) -> list:
	arr = reverse_arr(reverse_arr(arr[:d]) + reverse_arr(arr[d:]))
	return arr


arr = [1, 2, 3, 4, 5]
d = 14

if d > len(arr):
	d %= len(arr)

print(method_1(arr.copy(), d))
print(method_2(arr.copy(), d))
print(method_3(arr.copy(), d))
