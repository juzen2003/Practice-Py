# import re
# s = "co-vims-v1490874999_001_ir"
# p = ".*\_001\_ir"
# p1 = "ko"
#
# prog = re.compile(p)
# res = prog.match(s)
#
# print(res)

# import functools
#
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice
#
# @do_twice
# def say_hi(name):
#     print("hi %s" %(name))
#     return "hello %s" %(name)
#
# x = say_hi("John")
# print(x)
d1 = {"a": 'value1', "another": 'value12'}
d2 = {"a": 'value2', "other": "value22"}
d3 = {**d1, **d2}
print(d3)
