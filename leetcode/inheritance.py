# class car:
#     s_no = 20
#
#     def __init__(self):
#         self.name = ""
#         self.__lastName = "singh"
#
#
# c1 = car()
# print(c1.s_no)
# c1.s_no = 35
# print(c1.s_no)
# print(c1.__dict__)
# print(car.s_no)

# c1.name = "Bhawani"
# c1.__lastName = "Rathore"
# print(c1.name)
# print(c1._car__lastName)
# print(c1.__lastName)
# print(c1.__dict__)

# class model(car):
#     print("model")
#
#     def __init__(self):
#         self.message = "hello"
#         # print(message)


# class Person:
#
#     def __init__(self, ):
#         self.name = ""
#         self.age = 0
#
#     @staticmethod
#     def checkAge(age):
#         if int(age) > 18:
#             print("adult")
#         else:
#             print("child")
#
#
# Person.checkAge(20)


# class Parent:
#     def call_child_method(self, child_instance):
#         print("Calling child method from parent")
#         child_instance.child_method()
#
#
# class Child(Parent):
#     def child_method(self):
#         print("Child method called")
#
#
# # Creating an instance of the child class
# child_instance = Child()
#
# # Calling the method in the parent class that accesses the child method
# parent_instance = Parent()
# parent_instance.call_child_method(child_instance)


class Parent:

    def __init__(self, name):
        self.__name = name
        self.__private = "private"

    def add(self, a, b):
        return a + b


class Child(Parent):
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age


c = Child(20, "bhawani")
# print(c.age)
print(c._Parent__name)

# print(c.add(10, 5))
print(c._Parent__private)

# class Patent:
#
#     def __init__(self, name):
#         self.name = name
#         self.__private = "private"
#
#     def func(self, a, b):
#         return a + b
#
#
# class Child(Patent):
#     def __init__(self, age, name):
#         super().__init__(name)
#         self.age = age
#
#     def func(self, a, b):
#         return a - b
#
#
# c = Child(20, "bhawani")
# print(c.func(10, 5))
# print(c.age)
# print(c.name)
#
# print(c.func(10, 5))
# print(c._Patent__private)
