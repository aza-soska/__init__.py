#1
# a=[1,2,3,4,5,6]
# a.reverse()
# print(a)
#2
# a=[7,3,5,4,2,6,9]
# a.sort()
# print(a[-1])
# print(a[0])
#3
# a=[2,4,6,4,9,2,1]
# x=0
# y=0
# for i in a:
#     x+=i
#     y+=i / len(a)
# print(x)
# print(y)
#4
# a=[1,3,5,4,2,1,7,1]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#5
# a=[2,3,7,1,4,8,9]
# a.sort()
# print(a)
# a.reverse()
# print(a)
#6
# a=[3,6,1,2]
# a.pop(2)
# a.insert(2,4)
# print(a)
#7
# a=[1,2,5,3,2,2,5]
# x=0
# for i in a:
#     if i==2:
#         x+=1
# print(x)
#8
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
#9
# a=[1,2,3,4,5,6]
# x=[]
# y=[]
# for i in a:
#     if i%2==0:
#         x.append(i)
#     else:
#         y.append(i)
# print(x)
# print(y)
#10
# a=[2,5,3,1,8,6]
# a.sort()
# x=a[-2]
# print(x)

      #SET
#2
# a={1,2,3,4}
# b={1,2,4,3}
# if a==b:
#     print("true")
# else:
#     print("false")
#3
# x={2,4,32,5,6}
# print(len(x))
# x=sorted(x)[-1]
# print(x)
#4
# a={1,2,3,4,5,6,7,8,9,10}
# b=[]
# for i in a:
#     x=i**2
#     b.append(x)
# x=set(b)
# print(x)
#5
# A={1,3,2,6,5,8}
# B={1,3,2}
#
# print(B.issubset(A))
#6
# x={1,2,3,4,5,67,8}
# b=int(input())
# a=[]
# for i in x:
#     if i==b:
#         continue
#     a.append(i)
# c=set(a)
# print(c)


#1
# a=[1,2,3,2,1]
# x=len(set(a))
# print(x)

#2
a=[1,3,2]
b=[4,3,2]
