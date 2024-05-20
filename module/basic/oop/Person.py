class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)


class Student(Person):
    __family_name: str
    __last_name: str

    def __init__(self, fname: str, lname: str, age: int):
        Person.__init__(self, fname, age)
        self.__family_name = fname
        self.__last_name = lname

    def __str__(self):
        return self.__family_name + " " + self.__last_name + " " + str(self.age)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value


# p1 = Person("Thử xem", 2)
# print(p1.name)
# print(p1.age)

# x = Student("Mike", "Olsen", 2019)
# print(str(x.__last_name))


