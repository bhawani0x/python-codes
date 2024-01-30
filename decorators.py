def smart_div(func):
    # print("smart_div")
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


@smart_div
def div(a, b):
    print(a/b)

if __name__ == '__main__':
    # div = smart_div(div)
    div(12, 40)