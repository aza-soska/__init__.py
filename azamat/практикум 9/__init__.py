# #1
# def one(lst,y):
#     for t in range(len(lst)):
#         if lst[t] == y:
#             return y
#     return False
# def two(lst,z):
#     a = [48, 92, 1, 7, 34, 56]
#     for u in range(len(lst)):
#         if lst[u] == z:
#             return a[u]
#     return False
# def three(s,d):
#     if s%d==0:
#         return s
#     elif s%d!=0:
#         return d
#     return False
# a=[48, 92, 1, 7, 34, 56]
# x=[]
# for i in a:
#     x.append(i//10+i%10)
# print(one(a,max(a)),two(x,max(x)),three(one(a,max(a)),two(x,max(x))))


#2
# def two(lst,x):
#     a=0
#     b=len(lst)-1
#     while a<=b:
#         c=(a+b)//2
#         if x==lst[c]:
#             return True
#         elif x<lst[c]:
#             b=c-1
#         else:
#             a=c+1
#     return False
# print(two([2, 5, 8, 12, 16, 23, 38, 56],23))

#3
# def three(lst,x):
#     for i in range(len(lst)):
#         if lst[i] == x:
#             return x
#     return False
# a=[12, 99, 234, 7, 88, 42]
# print(three(a,max(a)))

#4
# def four(lst,x):
#     a=0
#     b=len(lst)-1
#     while a<=b:
#         c=(a+b)//2
#         if x==lst[c]:
#             return True
#         elif x<lst[c]:
#             b=c-1
#         else:
#             a=c+1
#     return a
# print(four([1, 4, 6, 9, 15],8))

#5
# def five(lst,x):
#     for i in range(len(lst)):
#         if lst[i] == x:
#             return True
#     return False
# print(five(["Alice", "Bob", "Charlie", "Diana", "Eva"],"Charlie"))


#6
# def six(lst,x):
#     a=0
#     b=len(lst)-1
#     while a<=b:
#         c=(a+b)//2
#         if x==lst[c]:
#             return True
#         elif x<lst[c]:
#             b=c-1
#         else:
#             a=c+1
#     return False
# print(six(["apple", "banana", "carrot", "grape", "orange", "peach"],"orange"))

#7
def seven(lst,x):
    a=0
    b=len(lst)-1
    while a<=b:
        c=(a+b)//2
        if x==lst[c]["id"]:
            return lst[c]["name"]
        elif x<lst[c]["id"]:
            b=c-1
        else:
            a=c+1
    return False
print(seven([

{"id": 101, "name": "Alex"},

{"id": 215, "name": "Max"},

{"id": 340, "name": "Anna"},

{"id": 540, "name": "Tim"}
]  ,340))

#8
# def closest_num(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#
#         if nums[mid] == target:
#             return nums[mid]
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     if right < 0:
#         return nums[left]
#     if left >= len(nums):
#         return nums[right]
#
#     if abs(nums[left] - target) < abs(nums[right] - target):
#         return nums[left]
#     else:
#         return nums[right]
#
# nums = [2, 5, 9, 14, 20]
# target = 7
# print(closest_num(nums, target))

#9
# def one(lst,x):
#     if lst!=sorted(lst):
#         for i in range(len(lst)):
#           if lst[i] == x:
#             return True
#         return False
#     elif lst==sorted(lst):
#       a=0
#       b=len(lst)-1
#       while a<=b:
#         c=(a+b)//2
#         if x==lst[c]:
#             return True
#         elif x<lst[c]:
#             b=c-1
#         else:
#             a=c+1
#       return False
#
# print(one([1, 3, 8, 12, 20],12))