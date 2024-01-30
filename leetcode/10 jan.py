class xyz:
    def __init__(self, name, student_class):
        self.name = name
        self.student_class = student_class

    def get(self):
        print("Hello")
        return self.name, self.student_class


class Student(xyz):

    def __init__(self, name, student_class):
        self.name = name
        self.student_class = student_class

    def get(self):
        super().get()
        return self.name, self.student_class


s = Student(name="Bhawani", student_class="BCA")

print(s.get())