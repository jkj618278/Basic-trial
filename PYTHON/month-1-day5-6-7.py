# name = input("Enter employee name : ")
# age = int(input("Enter employee age : "))
# salary = int(input("Enter employee salary : "))
# print(f"Employee name : {name}, age : {age} and salary : {salary}")


# string_data = '13'
# c = int(string_data)
# print(string_data , c)
# print(f"{type(string_data)} converted into {type(c)}")


# list_sales = [1,2.1,3,4,5,8,2.1,1]
# print(f''' Total sales : {sum(list_sales)} 
# Maximum sales : {max(list_sales)} and 
# Minimum sales : {min(list_sales)} ''')


# print(list_sales)
# list_sales = set(list_sales) #set output without duplicates
# print(list_sales)
# a = list(set(list_sales)) #list output without duplicates
# print(a)


# for i in range(1,101):
#     print(i)

# l = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in l:
#     if(i % 2 == 0):
#         sum += i
# print(sum)

# count = 0
# for i in l:
#     if(i > 5):
#         count += 1
# print(count)

# marks = {}
# for i in range(2):
#     student = input("Enter name : ")
#     m = int(input("Enter marks : "))
#     marks[student] = m
# c = max(marks.values()) 
# max(marks.values()) access maximum of values
# for key,data in marks.items():
#     if(data == c):
#         print(key)
#         print(data)
# key , data in marks.items() for printing value to key 

# text = "ant is ant but it is an animal"
# words = text.split() #list of string elements 
# print(words)
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)

# def average(a,b):
#     sum = (a+b) / 2
#     return sum

# def prime(a):
#     if(a == 1):
#         print("not a prime number")
#     else :
#         for i in range(2,a):
#             if(a % i == 0):
#                 print("not a prime number")
#                 break
#         else:
#             print("prime number")
# a = int(input("enter number to check it is prime or not : "))
# prime(a)

# import csv 

# with open("EXCEL/company.csv","r") as file:
#     table = csv.DictReader(file)
#     for data in table:
#         #for this you first make list then do it 
#         average = sum( [ int(data['sales']) ] ) / len( [ int(data['sales']) ] )
#     print(average)

# saless = []
# with open("EXCEL/company.csv","r") as f:
#     table = csv.DictReader(f)
#     for data in table:
#         saless.append(int(data['sales']))

# print(saless)
