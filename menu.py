import math
def menu():
    print("\n\n   menu \n 1. calculate \n 2. area \n 3. volume \n 4. exit ")
    ch = int(input("Enter your choice : "))
    if (ch == 1):
        calculate()
    elif (ch == 2):
        area()
    elif (ch == 3):
        volume()
    elif  (ch  == 4):
        exit
    
def calculate():
    print("\n \n 1. addition \n 2. subtraction \n 3. multiplication \n 4. division \n 5. power ")
    h = int(input('enter your choice : '))
    if (h ==1):
        a = float(input('enter your first value : '))
        b = float(input('enter your second value : '))
        c = a + b
        print('sum of two numbers is : ',c)
    elif (h == 2):
        a = float(input('enter your first value : '))
        b = float(input('enter your second value : '))
        c = a - b
        print('subtraction of two numbers is : ',c)
    elif (h == 3):
        a = float(input('enter your first value : '))
        b = float(input('enter your second value : '))
        c = a * b
        print('multiplication of two numbers is : ',c)
    elif (h == 4):
        a = float(input('enter your first value : '))
        b = float(input('enter your second value : '))
        c = a / b
        print('division of two numbers is : ',c)
    elif (h == 5):
        a = float(input('enter your first value : '))
        b = float(input('enter your second value : '))
        c = pow(a,b)
        print(' power of number is : ',c)
    ans  = input('do you want to continue and to go to main menu ? y /n ')
    if (ans == 'y'):
        menu()
    else :exit
def area():
    print("\n \n 1. square \n 2. rectangle \n 3. circle \n 4. triangle ")
    h = int(input('enter your choice : '))
    if (h ==1):
        a = float(input('enter your side of square : '))
        c = a * a
        print('area of square is : ',c)
    elif (h == 2):
        a = float(input('enter your first side : '))
        b = float(input('enter your second side : '))
        c = a * b
        print('area of rectangle is : ',c)
    elif (h == 3):
        a = float(input('enter your radius'))
        c = 3.14 * r *r
        print('area of circle is : ',c)
    elif (h == 4):
        a = float(input('enter your first side : '))
        b = float(input('enter your second side : '))
        d = float(input('enter your third side : '))
        s = (a + b + d)/2
        c = math.sqrt(s*(s-a)*(s-b)*(s-d))
        print('area of triangle : ',c)
    ans  = input('do you want to continue and to go to main menu ? y /n ')
    if (ans == 'y'):
        menu()
    else :exit
    
def volume():
    print("\n \n 1. cube \n 2. cuboid \n 3. sphere \n 4. cylinder ")
    h = int(input('enter your choice : '))
    if (h ==1):
        a = float(input('enter your side of  cube: '))
        c = a * a * a
        print('volume of cube is : ',c)
    elif (h == 2):
        a = float(input('enter your first side : '))
        b = float(input('enter your second side : '))
        d = float(input('enter your third side : '))
        c = a * b * d
        print('volume of cuboid is : ',c)
    elif (h == 3):
        a = float(input('enter your radius'))
        c = 3.14 * a * a * 4 / 3 
        print('volume of sphere is : ',c)
    elif (h == 4):
        a = float(input('enter your radius'))
        b = float(input('enter your height'))
        c = 3.14 * a * a * b
        print('volume of cylinder : ',c)    
    ans  = input('do you want to continue and to go to main menu ? y /n ')
    if (ans == 'y'):
        menu()
    else :exit
     
menu()

    
    
