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
### list manipulation
```py
l1 = ["John", "Mark", "Allen", "Mario"]
print l1 #['John', 'Mark', 'Allen', 'Mario']
l1[1] = "Kat"
print l1 #['John', 'Kat', 'Allen', 'Mario']
l1.insert(2, "Jason")
print l1 #['John', 'Kat', 'Jason', 'Allen', 'Mario']
del(l1[3])
print l1 #['John', 'Kat', 'Jason', 'Mario']
l1.remove("John")
print l1 #['Kat', 'Jason', 'Mario']
l1.append("Mary")
print l1 #['Kat', 'Jason', 'Mario', 'Mary']
l1.pop()
print l1 #['Kat', 'Jason', 'Mario']
l1.pop(1)
print l1 #['Kat', 'Mario']
```
