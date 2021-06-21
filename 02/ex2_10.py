class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):  # 메소드
        return self.first_name + " " + self.last_name

    def __str__(self):  # 특수 메소드
        return self.last_name + ", " + self.first_name

person1 = Person("John", "Smith")
print(person1.get_name())
print(person1)