#1
# a=[1,2,3,2,1]
# print(len(set(a)))

#2
# a=[1,3,2]
# b=[4,3,2]
# x=set(a) & set(b)
# print(len(x))

#3
# a="python"
# b="notebook"
# x=list(sorted(set(a) & set(b)))
# print(x)

#4
# math={"azamat","mansur","aidos"}
# cs={"aidos","beka"}
# physics={"azamat","dima"}
# q=math|cs|physics
# x=math & cs
# x1=math & physics
# y=x|x1
# print(q-y)

#5
# python_group = {"Айгүл", "Бекзат", "Данияр"}
# java_group = {"Айгүл", "Самат", "Лаура"}
# a=python_group & java_group
# b=python_group - java_group
# c=python_group | java_group
# print("екі курс:",a)
# print("тек пайтон:",b)
# print("кез келген курс:",c)

#6
# x = {}
#
# a = [("Ivanov", "paper"),
# ("Petrov", "pens"),
# ("Ivanov", "marker"),
# ("Ivanov", "paper"),
# ("Petrov", "envelope"),
# ("Ivanov", "envelope")]
#
# for name, item in a:
#     x[name] = x.get(name, set()) | {item}
# for name, items in x.items():
#     print(name, items)
#7
# a = "Мен Python жақсы көремін және python үйренемін"
# b=a.lower()
# x = b.split()
# c = {}
# for i in x:
#     c[i] = c.get(i, 0) + 1
# print(c)

#8
# prices = {"alma": 300, "banan": 450, "sut": 550}
#
# prices.pop("banan")
#
# prices.update({"almurt": 200,"orik": 400,"et": 1200,"kartop": 150,"kurt": 100})
#
# fruits = {"alma", "almurt", "orik"}
# dairy_meat_vegs = {"sut", "kurt", "et", "kartop"}
#
# for item in list(prices.keys()):
#     price = prices[item]
#     if item in fruits:
#         prices[item] = int(price * 1.20)
#     elif item in dairy_meat_vegs:
#         prices[item] = int(price * 1.30)
#
# print(prices)


#9
# a={"Azamat":90,"Mansur":10,"Aidos":80,"Bekzhan":70}
# x=max(a.values())
# y=min(a.values())
# z=sum(a.values()) / len(a.values())
# print("MAX:",x)
# print("MIN:",y)
# print("AVG:",z)


#10
# store = {"alma": 10, "banan": 5, "nan": 3}
#
# product = str(input("Қандай тауар аласыз: "))
# amount = int(input(f"Қанша {product} аласыз: "))
#
#
# if product in store:
#     if store[product] >= amount:
#         store[product] = store[product] - amount
#         print("Басында",amount,product, "сатып алынды. Қалғаны:", store[product])
#     else:
#         print("Жеткіліксіз! Қоймада", store[product], "ғана бар.")
#     amount2 = int(input(f"Екінші жолы қанша {product} аласыз: "))
#     if store[product] >= amount2:
#         store[product] = store[product] - amount2
#         print(product, "сатып алынды. Қалғаны:", store[product])
#     else:
#         print("Енді жеткіліксіз! Қоймада", store[product], "ғана бар.")
# else:
#     print("Мұндай тауар жоқ.")