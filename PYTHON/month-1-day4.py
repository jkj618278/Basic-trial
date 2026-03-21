# company_name = "Tyrant"
# sales = []
# employees = 40
# print(f"Company name : {company_name}")
# print(f"No. of employees : {employees}")

# day = 1
# week = day * 7
# for data in range(week):
#     sales.append(int(input(f"enter day {day} sale : ")))
#     day += 1
# total_revenue = sum(sales)
# print(f"total revenue in a week : {total_revenue}")
# print(f"sales : {sales}")
# print(f"Total sales = {total_revenue}")
# print(f"Average sales = {sum(sales)/ len(sales)}")

# print("Sales greater than 500 - ")
# count = 0
# for data in sales:
#     if(data > 500):
#         print(data)
#     if(data > 600):
#         count += 1
# print(f"Sales greater than 600 counting is {count}")

# sorted_sales = sorted(sales,reverse=True)[:3]
# print(f"Top 3 highest sales : {sorted_sales}")

# variety = 5
# product_values = {}
# for data in range(variety):
#     products = input("Enter the product : ")
#     product_prices = int(input("Enter the product price : "))
#     product_values[products] = product_prices 

# list1 = product_values.values()
# print(f"Product prices : {list1}")
# print(f"Highest price : {max(list1)}")

# import csv
# sales_list = [] 
# with open("EXCEL/company.csv",'r') as file:
#     content = file.read()
#     print(content)

#     file.seek(0) # 🔥 Reset pointer to start

#     table = csv.DictReader(file)  # file to dictionary formed
#     for data in table:
#         sales_list.append(int(data['sales'])) #value[key]
# print("Sales Column - ")
# print(sales_list)

'''
file.read() moves the file cursor to the end

So when DictReader(file) runs, there is nothing left to read

That's why your loop doesn't run and sales_list stays empty []

file.seek(0)  # 🔥 Reset pointer to start
'''

# import csv
# sales = []
# total_sales = 0
# with open("EXCEL/company.csv","r") as file:
#     table = csv.DictReader(file)
#     for data in table:
#         # total_sales += int(data['sales'])
#         sales.append(int(data['sales']))
#     file.seek(0)
#     content = file.read()
#     print(content)
# maximum_sales = max(sales)
# print(f"Total sales : {total_sales} and maximum sales : {maximum_sales}")
# def Totalsales(list):
#     total = sum(list)
#     return total
# def Avgsales(list):
#     average = sum(list) / len(list)
#     return average
# def Highestsales(list):
#     highest = max(list)
#     return highest

# print(f"Total sales : {Totalsales(sales)}")
# print(f"Average sales : {Avgsales(sales)}")
# print(f"Maximum sales : {Highestsales(sales)}")

# sorted_sales = sorted(sales,reverse=True)
# print(sorted_sales[:3])

# for data in sales:
#     if(data > Avgsales(sales)):
#         print(data)

sales = [12000,15000,9000,20000,18000,11000]
print(f"total = {sum(sales)}")
print(f"average = {sum(sales) / len(sales)}")
print(f"highest = {max(sales)}")
print(f"Top 3 sales : {sorted(sales,reverse=True)[:3]}")
