# Task 1
# a = [3, -1, 5, -2, 7, -4]
# x = []
# for i in a:
#     x.append(i)
#     if i < 0:
#         x.append(0)
# print(x)

# Task 2
# nums = [1, 2, 3, 2, 4, 2, 5]
# x = 2
#
# first = nums.index(x)
# last = len(nums) - 1 - nums[::-1].index(x)
#
# for i in sorted([first, last], reverse=True):
#     del nums[i]
#
# print(nums)

# Task 3
# t = (1, 2, 3)
# t = t + (4,)
# print(t)

# Task 4
# grades = [90, 75, 80, 100]
# avg = sum(grades) / len(grades)
# print("Орташа мән:", avg)

# Task 5
# nums = [2, 10, 4, 8, 6]
# total = min(nums) + max(nums)
# print("Қосынды:", total)

# Task 6
# a = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
#
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(even+odd)

# Task 7
# fruits = ['apple', 'banana', 'orange']
#
# if 'apple' in fruits:
#     print("Бар")
# else:
#     print("Жоқ")

# Task 8
# nums = (2, 4, 6, 8)
# product = 1
# for n in nums:
#     product *= n
# print("Көбейтінді:", product)

# Task 9
# ages = (18, 22, 30, 17)
#
# if any(a < 18 for a in ages):
#     print("Кәмелетке толмаған бар")
# else:
#     print("Барлығы кәмелетке толған")

# Task 10
# data = (1, 5, 9)
# total = sum(data)
#
# print("Қосынды:", total)
# if total > 10:
#     print("10-нан үлкен")
# else:
#     print("10 немесе кіші")

# Task 11
# t = (10, 20, 30)
# lst = list(t)
# lst.append(40)
# print(lst)

# Task 12
# nums = [10, 2, 8, 15, 3]
# diff = max(nums) - min(nums)
# print("Айырмасы:", diff)

# Task 13
# nums = [5, 2, 8, 3, 1, 4]
#
# even = [n for n in nums if n % 2 == 0]
# odd = [n for n in nums if n % 2 != 0]
# res = even + odd
#
# print(res)

# Task 14
# t = (10, 20, 30)
# a, b, c = t
# print("a =", a)
# print("b =", b)
# print("c =", c)

# Task 15
# lst = [1, 2, 3, 4, "abc"]
# lst.append("жүзім")
# lst.append("құлпынай")
#
# print("Барлығы:", len(lst), "элемент")
#
# numbers = [x for x in lst if type(x) == int]
# strings = [x for x in lst if type(x) == str]
#
# print("Сандар:", numbers)
# print("Жолдар:", strings)
