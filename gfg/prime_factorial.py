num = 315


def prime_factorial(num):
    if num == 1:
        print(num)
    else:
        for i in range(2, num):
            if num != 1:
                while (num % i == 0):
                    print(i)
                    num = num // i
            else:
                break


prime_factorial(num)
