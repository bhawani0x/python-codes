# Palindrome Check

string = "abcdcba"

# method 1
if string == string[::-1]:
	print("string is palindrome")

# method 2: recursion
def rec(s):
	n = len(s)
	if n==0 or n==1:
		return True
	else:
		if s[0] == s[-1]:
			rec(s[1:-1])
		else:
			return False

rec(string)
