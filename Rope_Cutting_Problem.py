# Rope Cutting Problem
def rope_cutting(n, a, b, c):
	if n == 0:
		return 0
	if n < 0:
		return -1

	result = max(rope_cutting(n - a, a, b, c), rope_cutting(n - b, a, b, c), rope_cutting(n - c, a, b, c))
	if result == -1:
		return result
	else:
		return result + 1


n = 5
a = 1
b = 2
c = 5

print(rope_cutting(n, a, b, c))
