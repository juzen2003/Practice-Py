# import re
# s = "co-vims-v1490874999_001_ir"
# p = ".*\_001\_ir"
# p1 = "ko"
#
# prog = re.compile(p)
# res = prog.match(s)
#
# print(res)

class Animal:
    # class variable
    animal_hi = "Hiii"
    # define instance variables when class object is init
    def __init__(self, name="", age=0, type=""):
        self.name = name
        self.age = age
        self.type = type

    def move(self):
        print(self.name + " is moving!")

dog1 = Animal("Lucky", 2, "Dog")
dog1.move() #Lucky is moving!
print(Animal.animal_hi) #Hiii

class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)

dog2 = Dog("Test", 2, "Dog")
dog2.move()
print(Dog.animal_hi)
