# Task 1
# a=int(input())
# x=0
# for i in range(1,a+1):
#     if i%2!=0:
#         x+=i**2
#
# print(x)

# Task 2
# n=input()
# if n==n[::-1]:
#     print("Иә")
# else:
#     print("Жоқ")

# Task 3
# a=int(input())
# x=0
# for i in range(1,a+1):
#     if a%i==0:
#       x+=1
# print(x)

# Task 4
# a=input()
# x=1
# y=False
# for i in a:
#     I=int(i)
#     if I%2!=0:
#         x*=I
#         y=True
# if y:
#     print(x)
# else:
#     print("0")

# Task 5
# x=0
# while True:
#     a=int(input())
#     if a==0:
#         break
#     x+=a
# print(x)

# Task 6
# N=int(input("Неше сан енгізесіз? "))
# x=int(input("1-сан:"))
# mini=x
# maxi=x
# for i in range(2,N+1):
#     num=int(input(str(i)+"-cан:"))
#     if num<mini:
#         mini=num
#     elif num>maxi:
#         maxi=num
# print("Ең кіші сан:",mini)
# print("Ең үлкен сан:",maxi)

# Task 7
# a=0
# i=0
# while a<=100:
#     i+=1
#     a+=i
# print(i)
# print(a)

# Task 8
# a=input("Жол: ")
# b=input("Таңба: ")
# x=0
# for i in a:
#     if i==b:
#         x+=1
# print(x)

# Task 9
# a=int(input())
# x=0
# for i in range(1,a+1):
#     print(i, end=" ")
#     x += i
# print("\n",x)

# Task 10
# a=int(input())
# for i in range(1,11):
#     print(str(a)+"+"+str(i)+"="+str(a*i))