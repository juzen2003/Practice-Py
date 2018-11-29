### python string interpolation
```py
# string interpolation
name = "John"
age = 23
res = "Hi my name is {}, I am {} years old".format(name, age)
res1 = "Hi my name is %s, I am %s years old" %(name, age)
res_for_python3 = f"Hi my name is {name}, I am {age} years old"
print(res)
print(res1)
print(res_for_python3) # we prefer this
# Hi my name is John, I am 23 years old
```

### repeat string
```py
hi_string = "hi"
print(hi_string * 3)
# hihihi
```

### repeat string
```py
hi = "hi here is replaced one"
print(hi.replace("here", "hi"))
# hi hi is replaced one
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
print(test[:3]) # Str
print(test[2:4]) # rI
print(test[2:2]) # nothing
print(len(test)) # 6
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

### class inheritance
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

dog1 = Animal("Lucky", 2, "Dog")
dog1.move() #Lucky is moving!
print(Animal.animal_hi) #Hiii

class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)

dog2 = Dog("Test", 2, "Dog")
dog2.move() #Test is moving!
print(Dog.animal_hi) #Hiii
```

### args (non-keyworded argument list)
```py
def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
# args = [1, 2, 3, 4, 5]
s = add(1,2,3,4,5)
print(s)
```

### kwargs (keyworded argument dictionary)
```py
def add(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum
# kwargs = {num1: 1, num2: 2, num3: 3, num4: 4, num5: 5}
s = add(num1=1, num2=2, num3=3, num4=4, num5=5)
print(s)
```

### dictionary
```py
d = {"a": 'value', "another": 'value2'}
d["item1"] = 2
d["item2"] = 23

print d # {'a': 'value', 'item2': 23, 'item1': 2, 'another': 'value'}

for key in d:
  print(key) # a item2 item1 another

for value in d.values():
  print(value) # value 23 2 value

print d.items() # [('a', 'value'), ('item2', 23), ('item1', 2), ('another', 'value')]

for k, v in d.items():
  print(k) # a item2 item1 another
  print(v) # value 23 2 value
```

### merge two dictionaries
```py
d1 = {"a": 'value1', "another": 'value12'}
d2 = {"a": 'value2', "other": "value22"}
d3 = {**d1, **d2}
print(d3)
# {'a': 'value2', 'another': 'value12', 'other': 'value22'}
```

### [] is a falesy value
```py
a = []
if not a:
  print("this will be run if a is []")
```

### regex
```py
import re
prog = re.compile(pattern)
result1 = prog.match(string)
#  same as
result2 = re.match(pattern, string)
```
