### python string interpolation
```py
# string interpolation
name = "John"
age = 23
res = "Hi my name is {}, I am {} years old".format(name, age)
res1 = "Hi my name is %s, I am %s years old" %(name, age)
print(res)
print(res1)
# Hi my name is John, I am 23 years old
```

### repeat string
```py
hi_string = "hi"
print(hi_string * 3)
# hihihi
```

### string lowercase uppercase
```py
test = "StrINg"
print(test.lower()) # string
print(test.upper()) # STRING
```

### string manipulation
```py
test = "StrINg"
print(test[1:]) # trINg
print(test[2:4]) # rI
print(test[2:2]) # nothing
```

### string split() & join()
```py
test = "StriNg is here"
print(test.split()) # ['strinG', 'is', 'here']
print(test.split("i")) # ['str', 'nG ', 's here']
#  join works for list of string only
l = ["3", "gt", "87"]
print("-".join(l)) # 3-gt-87
print("".join(l)) # 3gt87
```

### list manipulation
```py
l1 = ["John", "Mark", "Allen", "Mario"]
print(l1) #['John', 'Mark', 'Allen', 'Mario']
l1[1] = "Kat"
print(l1) #['John', 'Kat', 'Allen', 'Mario']
l1.insert(2, "Jason")
print(l1) #['John', 'Kat', 'Jason', 'Allen', 'Mario']
del(l1[3])
print(l1) #['John', 'Kat', 'Jason', 'Mario']
l1.remove("John")
print(l1) #['Kat', 'Jason', 'Mario']
l1.append("Mary")
print(l1) #['Kat', 'Jason', 'Mario', 'Mary']
l1.pop()
print(l1) #['Kat', 'Jason', 'Mario']
l1.pop(1)
print(l1) #['Kat', 'Mario']
print(len(l1)) #2
```

### for loop
```py
for x in range(1, 10):
    print(x) # this will print from 1 to 9

l1 = [2, 3, 6, 9, 10]
for item in l1:
    print(item) # this will print all items in order in l1
```

### class example
```py
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

dog = Animal("Lucky", 2, "Dog")
dog.move() #Lucky is moving!
print(Animal.animal_hi) #Hiii
```
