import math

a = float(input('enter first side : '))
b = float(input('enter second side : '))
c = float(input('enter third side : '))

d = (a+b+c)/2

area = math.sqrt(d*(d-a)*(d-b)*(d-c))
print('area of triangle', area)
