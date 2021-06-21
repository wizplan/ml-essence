class Person:  # Person 클래스 정의
    def __init __(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

person1 = Person("John", "Smith")  # ❶
print(person1.first_name, person1.last_name)

person2 = Person()  # ❷
person2.first_name = "Robert"  # ❸
person2.last_name = "Johnson"
print(person2.first_name, person2.last_name)