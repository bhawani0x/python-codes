import math
a = float(input('enter cofficent of x^2 : '))
b = float(input('enter cofficent of x : '))
c = float(input('enter numeric value : '))

d = b*b -(4*a*c)

if (d == 0):
    print('roots are real and equal')
    root = -b/(2*a)
    print('root : ', root)
elif (d > 0 ):
    print('roots area unequal but real')
    root = (-b + math.sqrt(d))/(2*a)
    root1 = (-b - math.sqrt(d))/(2*a)
    print('root 1 : ',root)
    print('root 2 : ',root1)
else :
    print('roots are imaginary ')
    d = -1*d 
    print('first root',-b/(2*a) ,'+',math.sqrt(d)/(2*a),'i')
    print('second root',-b/(2*a) ,'-',math.sqrt(d)/(2*a),'i')
