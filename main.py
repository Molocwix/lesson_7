# my_list = [1,2,3]
# iterator = iter(my_list)
#
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
#
# my_list = [1,2,3]
# interator = iter(my_list)
#
# for elem in interator:
#     print(elem)
# for elem in interator:
#     print(elem)
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print(elem)
# def raise_to_the_degrees(number, max_degree):
#  i=0
#  for _ in range(max_degree):
#     yield number**i
#     i+=1
# res = raise_to_the_degrees(122345, 500)
# print(res)
# for _ in res:
#  print(_)
# def raise_to_the_degrees(number):
#     i=0
#     while True:
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)
# def raise_to_the_degrees(number):
#     i=0
#     while True:
#         result = number**i
#         yield result
#         if result> 100**20:
#             return
#         i+=1
# res = raise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)
# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
#
# helper = Helper("homework")
# print(helper("cleaning"))
# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return helper
# def helper(work):
#      work_in_memory = work
#
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will  help you with {work}"
#
#     return helper
#
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))
# def checker(function, *args, **kwargs):
#     def calculate(expression):
#         return eval(expression)
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have problems {exc}")
#     else:
#         print(f"No problems. Result –  result")
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result –  {result}")
#     return checker
# @checker
# def calculate(expression):
#     return eval(expression)
# calculate = checker(calculate)
# calculate("2+2")

# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 result = function(*args,**kwargs)
#              except (exc_types) as exc:
#                 print(f"We have problems {exc}")
#              else:
#                 print(f"No problems. Result –  {result}")
#     return checker
#     return checker
# @checker(NameError, TypeError, SyntaxError)
# def calculate(expression):
#     return eval(expression)

# calculate("2+2")


