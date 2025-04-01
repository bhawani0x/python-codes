# Generate Subsets

def subsets(s, cur, index):
	if index == len(s):
		print(cur)
		return
	subsets(s, cur, index+1) # exclude
	subsets(s, cur+s[index], index+1) #include


string = "abc"
# ans: a, b, c, ab ,bc, ca, abc, "". hence total number os subsets are equal to 2^n where n is length of string
subsets(string,"", 0)
