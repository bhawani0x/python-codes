# Sum of Digits Using Recursion
# eg. 235 = 2 + 3 + 5 = 10

def sum_of_digits(sum, num):
	sum = sum + num % 10
	if num > 9:
		sum_of_digits(sum, num // 10)
	else:
		print(sum)


num = 235
sum = 0
sum_of_digits(sum, num)
