# LCM of 2 number is equal to  product of two number divided by HCF of two number

a = 4
b = 6

def HCF(a, b):
    if a%b == 0:
        return b
    else:
        return HCF(b, a%b)

lcm = a*b//HCF(a,b)
print(lcm)