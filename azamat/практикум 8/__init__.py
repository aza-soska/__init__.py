#1
# def one(n):
#     if n==1:
#         print("yes")
#         return
#     if n<=0 or n%2==1:
#         print("no")
#         return
#     one(n//2)
# a=int(input())
# one(a)

#2
# def two(n,a=2):
#     if n==1:
#         return
#     if n%a==0:
#         print(a,end=" ")
#         two(n//a,a)
#     else:
#         two(n,a+1)
# N = int(input())
# two(N)

#3
# def three(n,a=1):
#     if n==0:
#         return
#     b=min(n,a)
#     def repeat(n1,a1):
#         if a1==0:
#             return
#         print(n1,end=" ")
#         repeat(n1,a1-1)
#     repeat(a,b)
#     three(n-b,a+1)
# three(int(input()))

#4
# def four(n,a=0):
#     if n==0:
#         return a
#     return four(n//10,a*10+n%10)
# print(four(int(input())))

#5
# def gsd(a, b):
#     if b == 0:
#         return a
#     return gsd(b, a % b)
# def lsm(a, b):
#     return abs(a * b) // gsd(a, b)
# print(lsm(int(input()), int(input())))
