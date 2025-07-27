# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

class Calculate:
    _instance = None  # class variable to hold the single instance

    def __new__(cls, a, b):
        if cls._instance is None:
            cls._instance = super(Calculate, cls).__new__(cls)
        return cls._instance

    def __init__(self, a, b):
        self.val_a = a
        self.val_b = b

    def is_multiple(self):
        return self.val_a % self.val_b == 0
     
ob = Calculate(2, 4)
print("--------",ob,"--------")
print(ob.is_multiple())

ob1 = Calculate(4,2)
print("--------",ob1,"--------")
print(ob.is_multiple())

ob2 = Calculate(4,16)
print("--------",ob2,"--------")
print(ob.is_multiple())

ob3 = Calculate(4,4)
print("--------",ob3,"--------")
print(ob.is_multiple())

