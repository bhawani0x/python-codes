a = 24
b = 9
# method 1:
GCD = a if a < b else b
for i in range(GCD):
    if b % GCD == 0 and a % GCD == 0:
        print(f"GCD is {GCD}")
        break
    else:
        GCD -= 1

# method 2: Euclidean algorithm
ma = max(a,b)
mi = min(a,b)
def gcd(ma, mi):
    if ma==mi:
        return ma
    else:
        ma = ma-mi
        return gcd(max(ma,mi),min(ma,mi))

print(gcd(ma,mi))

# Method 3: Advanced Euclidean algorithm

def ad_gcd(max, min):
    if max%min==0:
        return min
    return ad_gcd(min, max%min)

print(ad_gcd(ma,mi))