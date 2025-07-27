# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators

class Demo:
    
    _instance = None

    def __new__(cls, *ags):
        if cls._instance is None:
            cls._instance = super(Demo, cls).__new__(cls)
        return cls._instance

    def __init__(self, num: int)-> None:
        self.num = num

    def check_even(self)->None:
        if self.num & 1 == 0:
            print(True)
        else:
            print(False)


ob = Demo(44)
ob.check_even()

