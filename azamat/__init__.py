file  = open("shop_logs.txt", "r")
unique_users = set()
total_buys = 0
total_sum = 0
user_spending = {}
for line in file:
    parts = line.strip().split(";")
    user_id = parts[1]
    print(user_id)
    action = parts[2]
    unique_users.add(user_id)
    if action == "BUY":
        total_buys += 1
        amount = int(parts[3])
        total_sum += amount
        if amount not in user_spending:
            user_spending[user_id] = amount
        else:
            user_spending[user_id] += amount
file.close()

max_user=""
max_spent=0
for user in user_spending:
    if user_spending[user] > max_spent:
        max_spent = user_spending[user]
        max_user = user
if total_buys > 0:
    bill= total_sum/total_buys
else:
    bill = 0
report= open("report.txt","w" , encoding="utf-8")
report.write("Уникальных пользователей: " + str(len(unique_users)) + "\n")
report.write("Всего покупок: " + str(total_buys) + "\n")
report.write("Общая сумма: " + str(total_sum) + "\n")
report.write("Самый активный покупатель: " + max_user + "\n")
report.write("Средний чек: " + str(bill) + "\n")
report.close()
print("Отчет успешно создан!")

data = """name,department,salary
Ali,IT,500000
Dana,HR,300000
Arman,IT,600000
Aruzhan,Marketing,400000
Dias,IT,450000"""
with open("employees.csv", "w") as f:
    f.write(data)


import csv
all_employees = []
dept_salary = {}
with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        salary = int(row["salary"])
        dept = row["department"]
        all_employees.append(row)
        row["salary"] = salary
        if dept not in dept_salary:
            dept_salary[dept] = []
        dept_salary[dept].append(salary)

total_salary = sum(i["salary"] for i in all_employees)
avg_total = total_salary / len(all_employees)

dept_averages = {}  #орташа dept
for dept, salary in dept_salary.items():
    avg = sum(salary) / len(salary)
    dept_averages[dept] = avg

best_dept_name = max(dept_averages, key=dept_averages.get)
best_dept_value = dept_averages[best_dept_name]
richest_emp = max(all_employees, key=lambda i: i["salary"])
print(f"Орташа жалақы: {avg_total}")
print(f"Ең бай бөлім: {best_dept_name} ({best_dept_value})")
print(f"Ең бай қызметкер: {richest_emp['name']}")


q = []
for i in all_employees:
    if i["salary"] > avg_total:
        q.append(i)

with open("high_salary.csv", "w", encoding="utf-8") as f:
    columns = ["name", "department", "salary"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(q)
print("\n")
with open("high_salary.csv", "r", encoding="utf-8") as f:
    q = csv.reader(f)
    for i in q:
        print(i)

import json
data = [
  {
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },
  {
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  },
  {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
  }
]
with open("orders.json", "w") as f:
    json.dump(data, f, indent=4)

import json
with open("orders.json", "r") as f:
        data = json.load(f)

total_revenue = 0
user_order_counts = {}
item_counts = {}
richest_order = None
max_price = 0
for i in data:
    total_revenue += i["total"]

    user = i["user"]    # читаем з к.п
    if user in user_order_counts:
        user_order_counts[user] += 1
    else:
        user_order_counts[user] = 1

    if i["total"] > max_price:
        max_price = i["total"]
        richest_order = i

    for j in i["items"]:
        if j in item_counts:
            item_counts[j] += 1
        else:
            item_counts[j] = 1
q = None
w = 0
for item, count in item_counts.items():
    if count > w:
        w = count
        q = item

top_user = richest_order["user"] if richest_order else None

resalt = {"total_revenue": total_revenue,
    "top_user": top_user,
    "most_popular_item": q,
    "total_orders": len(data)}
with open("summary.json", "w") as f:
    json.dump(resalt, f, indent=4)

with open("summary.json", "r") as f:
    print(f.read())

data = """user_id,amount
user_1,5000
user_2,10000
user_1,700000
user_3,3000
user_2,900000
user_4,2000"""
with open("transactions.csv", "w") as f:
    f.write(data)
import csv
import json

a=[]
b=set()
c={}
with open("transactions.csv", "r") as f:
    reader=csv.DictReader(f)
for i in reader:
