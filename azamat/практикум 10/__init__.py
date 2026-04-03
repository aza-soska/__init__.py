#1# Part 1
# Task 1
# check = lambda x : "Положительное" if x > 0 else "Отрицательное" if x < 0 else " Ноль"
# print(check(5))
# print(check(-3))
# print(check(0))

# Task 2
# words = ["арбуз", "кот", "машина", "дом", "ананас"]
# result =  sorted(words, key=lambda x:len(x) )
# print(result)

# Task 3
# numbers = [5, 12, 7, 20, 33, 8]
# result = list(filter(lambda x: x % 2 == 0 and x > 10, numbers))
# print(result)

# Task 4
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(map(lambda x: x*x if x % 2 == 0 else x*3,numbers))
# print(result)

# Task 5
# check = lambda a,b: "a больше" if a>b else "b больше" if a<b else "Равны"
# print(check(1,2))
# print(check(3,1))
# print(check(4,4))

# Task 6
# numbers = [0, -3, 5, -7, 8]
# result = [(lambda x: "Положительное" if x > 0  else "Отрицательное" if x < 0 else "Ноль")(x)for x in numbers]
# print(result)

# Part 2
# Task 1
# def even_numbers(n):
#     result = []
#
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             if i % 4 == 0:
#                 result.append("кратно 4")
#             else:
#                 result.append(i)
#
#     return result
#
#
# for x in even_numbers(10):
#     print(x)

# Task 2
# def filter_words(words):
#     result = []
#
#     for word in words:
#         if len(word) > 4:
#             if "а" in word:
#                 result.append("с а")
#             else:
#                 result.append(word)
#
#     return result
#
#
# words = ["кот", "машина", "арбуз", "дом"]
#
# for w in filter_words(words):
#     print(w)

# Task 3
# def infinite_numbers():
#     i = 1
#
#     while True:
#
#         if i % 3 == 0 and i % 5 == 0:
#             yield "FizzBuzz"
#
#         elif i % 3 == 0:
#             yield "Fizz"
#
#         elif i % 5 == 0:
#             yield "Buzz"
#
#         else:
#             yield i
#
#         i += 1
# gen = infinite_numbers()
#
# for _ in range(15):
#     print(next(gen))

# Task 4
# def squares(n):
#     result = []
#
#     for i in range(1, n+1):
#         if i*i % 2 == 0:
#             result.append("Четный квадрат")
#         else:
#             result.append(i*i)
#
#     return result
#
# for x in squares(10):
#     print(x)

# Part 3
# Task 1
# squares = [x**2 for x in range(1, 21) if x % 2 == 0]
# print(squares)

# Task 2
# from functools import reduce
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# products = [reduce(lambda a, b: a * b, x) for x in matrix]
# print(products)

# Task 3
# words = ["кот", "машина", "ананас", "дом"]
#
# new_list = [word for word in words if len(word) > 4 and "а" not in word]
# print(new_list)

# Task 4
# numbers = [1, 2, 3, 4, 5]
#
# new_list = ["Четное" if num % 2 == 0 else "Нечетное" for num in numbers]
# print(new_list)

# Task 5
# matrix = [[1,2], [3,4], [5,6]]
#
# result = [num for row in matrix for num in row]
#
# print(result)

# Task 6
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#
# new_list = ["FizzBuzz" if x % 3 == 0 and x % 5 == 0
#             else "Fizz" if x % 3 == 0
#             else "Buzz" if x % 5 == 0
#             else x
#             for x in numbers]
# print(new_list)

# Part 4
# Task 1
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# def special_numbers(n):
#     for i in range(1, n + 1):
#
#         if i % 3 == 0 and i % 5 == 0:
#             yield "FizzBuzz"
#
#         elif i % 3 == 0:
#             yield "Fizz"
#
#         elif i % 5 == 0:
#             yield "Buzz"
#
#         elif is_prime(i):
#             yield "простое"
#
#         else:
#             yield i
#
#
# for x in special_numbers(15):
#     print(x)

# Task 2
# words = ["кот", "машина", "арбуз", "дом", "ананас"]
#
# result = [
#     (lambda w: (w.upper() if len(w) > 4 else "short") + ("*" if "а" in w else ""))(word)
#     for word in words
# ]
#
# print(result)

# Task 3
# def process_numbers(numbers):
#
#     filtered = filter(lambda x: x >= 0, numbers)
#
#     transformed = map(
#         lambda x: x / 2 if x % 2 == 0 else x * 3 + 1,
#         filtered
#     )
#
#     for num in transformed:
#         yield num
#
#
# numbers = [5, -2, 8, 0, -7, 3]
#
# for x in process_numbers(numbers):
#     print(x)

# Task 4
# students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
#
# grade_level = lambda g: (
#     "Отлично" if g >= 90
#     else "Хорошо" if g >= 70
#     else "Удовлетворительно"
# )
#
# result = {
#     name: grade_level(score)
#     for name, score in students
# }
#
# print(result)

# Task 5
# def matrix_transform(matrix):
#
#     for row in matrix:
#         for x in row:
#
#             if x % 2 == 0 and x % 3 == 0:
#                 yield "кратно 6"
#
#             elif x % 2 == 0:
#                 yield "чётное"
#
#             elif x % 3 == 0:
#                 yield "кратно 3"
#
#             else:
#                 yield x
#
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for x in matrix_transform(matrix):
#     print(x)

# Part 5
# Task 1
# numbers = [1,2,3,4,5]
# doubled = list(map(lambda x: x*2, numbers))
# print(doubled)

# Task 2
# words = ["кот", "машина", "арбуз", "дом"]
# result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
# print(result)

# Task 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)

# Task 4
# numbers = [0,5,12,7,20,-3,8]
# result = list(map(lambda x: x/2 if x % 2 == 0 else x*3,
# filter(lambda x:x>5,numbers)))
# print(result)