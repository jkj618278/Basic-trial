# calculate sales , cost , and profit of product in company
# Product = "I-PHONE"
# Quantity = 12
# Unit_price = 90000
# Sell_price = 100000
# cost = Unit_price * Quantity
# sales = Sell_price * Quantity
# Profit = sales - cost
# print(f"The products are {Product}")
# print(f"The cost of products are Rs.{cost}")
# print(f"The sales of products are Rs.{sales}")
# print(f"The profit of products are Rs.{Profit}")

# conversion of datatype to another datatype
# string_a = "23"
# string_b = "23"
# string_c = int(string_a)
# string_d = int(string_b)
# print(f"Total - {string_c + string_d}")

# check data types of differ columns
# columns = [1,0.2,"aman",False,None,12]
# for i in columns:
#     print(f"Element - {i} and Data_type - {type(i)} \n")

# small program that can only store user data as sales data , total sales
# , highest sales , lowest sales , remove duplicates , sort sales and avg sales
sales_data = []
ranges = int(input("enter the weeks that you have to store : "))
for i in range(0,ranges):
    sales_data.append(int(input()))
# print(f"sales data of {ranges} weeks are {sales_data}")
print(f"| Sales Data of {ranges} Weeks |")
for data in sales_data:
    print(f"| Rs. {data} |")

total_sales = sum(sales_data)
print(f"Total sales is Rs. {total_sales} \n")

highest_sales = max(sales_data)
print(f"Highest sale is Rs. {highest_sales}")

lowest_sales = min(sales_data)
print(f"Lowest sale is Rs. {lowest_sales}")

updated_sales_data = list(set(sales_data))
print(f"Updated sales data - {updated_sales_data} \n")

sort_sales = sorted(sales_data)   #reverse = true if desc
print(f"Sort sales data - {sort_sales}")

avg_sales = sum(sales_data) / len(sales_data)
print(f"Average sale is Rs. {avg_sales}")