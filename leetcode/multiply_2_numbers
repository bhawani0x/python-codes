def add(num_1, num_2):
	num_1 = num_1[::-1]
	num_2 = num_2[::-1]
	carry = 0
	sum = ""
	for i in range(max(len(num_1), len(num_2)) + 1):
		d_1 = 0 if i >= len(num_1) else num_1[i]
		d_2 = 0 if i >= len(num_2) else num_2[i]
		tmp_sum = carry + int(d_1) + int(d_2)
		carry = tmp_sum // 10
		sum += str(tmp_sum % 10)
	return sum[::-1]


def multiply_single(num, digit):
	digit = int(digit)
	num = num[::-1]
	ans = ""
	carry = 0
	for x in num:
		mul = int(x) * digit + carry
		ans += str(mul % 10)
		carry = mul // 10
	if carry:
		ans += str(carry)
	ans = ans[::-1]
	return ans


def multiply(a, b):
	ans = "0"
	b = b[::-1]
	for index, x in enumerate(b):
		ans = add(ans, multiply_single(a, x) + '0' * index)
	return ans


a = "2236723627367823286482376328462846238462384623846238462384623846238423648432648236482364823462836482364823648236482327"
b = "236723672632347236427834628396428376478236487236872364782364782634723487623478236478236478236448632487623846872364872634872364872364873648723648723647826347862346872634872634876234682364783624862378643278646763"
val = multiply(b, a)
print(val, int(val) == int(a) * int(b))
