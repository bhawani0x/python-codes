# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

class Demo:

    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super(Demo,cls).__new__(cls)
        return cls._instance
    
    def __init__(self, data:list)-> None:
        self.data = data
        
    def minmax(self)-> tuple:
        if len(self.data) == 1:
            return (self.data[0], self.data[0])
        elif len(self.data) >= 2:
            minimum = self.data[0]
            maximum = self.data[0]
            for counter in self.data[1:]:
                if counter > maximum:
                    maximum = counter
                if counter < minimum:
                    minimum = counter
            return (minimum, maximum)

ob = Demo([1,2,3,5,3,2,3,555,23,2,4,2,0,2,34])
print(ob.minmax())



