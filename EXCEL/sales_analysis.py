# file access
import csv

# sales data stored
sales_list = []

# file grant and use 
# error shown in this line because of main folder so change the path
# new path is excel/sales
with open("EXCEL/SALES.csv","r") as file: 
    table = csv.DictReader(file)  # file to dictionary formed
    for data in table:
        sales_list.append(int(data['sales'])) # data as values and sales as key , value[key]

average_sales = sum(sales_list) / len(sales_list)
print(f"Average Sales of the company is Rs.{average_sales}") 

top_sales = sorted(sales_list,reverse=True)
for i in top_sales[:5]:
    print(i)
# top_sales = sorted(sales_list,reverse=True)[:5]
# print(f"The top five sales in the company are {top_sales}")
