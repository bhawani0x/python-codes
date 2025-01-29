# check if number is palindrom number or not using mathamatical operation 

if __name__ == "__main__":
    x = 1234
    rem = 0
    while(x!=0):
        rem = rem*10+x%10
        x= x//10
    if rem == x:
        print(True)
    else:
        print(False)