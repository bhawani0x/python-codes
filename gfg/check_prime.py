num = 13


def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2,num):
            if num > i**i:
                if num%i == 0:
                    return False
            else:
                return True
print(check_prime(num))