#1
# def IsAscending(A):
#     i = 1
#     while i < len(A):
#         if A[i] <= A[i-1]:
#             return "NO"
#         i += 1
#     return "YES"
# print(IsAscending([1,7,9]))

#2
# def azamat(a):
#     x = a[0]
#     y = 0
#     for i in range(len(A)):
#         if a[i] > x:
#             x = a[i]
#             y = i
#         elif a[i] == x:
#             y = i
#     return x, y
# print(azamat([1,2,1,2,1]))

#3
# def azamat():
#     a = [0] * 10
#     while True:
#         x = int(input())
#         if x == 0:
#             break
#         if 1 <= x <= 9:
#             a[x] += 1
#     for i in range(1, 10):
#         print(a[i], end=" ")
# azamat()

#4
# def selsort(a):
#     a = a[:]
#     n = len(a)
#     for i in range(n):
#         x = i
#         for j in range(i+1, n):
#             if a[j] < a[x]:
#                 x = j
#         a[i], a[x] = a[x], a[i]
#     return a
#
# def azamat(dist, price):
#     price = selsort(price)
#     dist = selsort(dist)[::-1]
#     x = 0
#     for i in range(len(dist)):
#         x += dist[i] * price[i]
#     return x
# print(azamat([20, 40, 30],[50,20,30] ))

#5
# def bubble_sort(a):
#     a = a[:]
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# def azamat(a):
#     sorted_a = bubble_sort(a)
#
#     for x in sorted_a:
#         if -x in sorted_a:
#             i = a.index(x)
#             j = a.index(-x)
#             if i < j:
#                 return i, j
#             else:
#                 return j, i
#     return None
# print(azamat([1, 2, 3, -2, -4]))

#6
# def azamat(x, y):
#     y.sort()
#     a = 0
#     for i in y:
#         for j in x:
#             while j>i:
#                 a+=1
#                 j-=i
#             break
#     return a
# print(azamat([100],[40,90,50,60]))
# 100 100 100
# 4
# 40 90 50 60

#7
# def azamat(x, y):
#     y.sort()
#     a = 0
#     b = x
#     for i in y:
#         if i >= b:
#             a += 1
#             b = i + 3
#     return a
# print(azamat(60, [60, 63]))
# print(azamat(26, [30, 35, 40, 41, 42]))