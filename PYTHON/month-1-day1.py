# name = str(input("enter your name : "))
# age = int(input("enter your age : "))
# salary = float(input("enter your salary : "))
# print(f"Hi, {name}.You are {age} years old and this is your salary : {salary} monthly")

# salary = float(input("enter your salary : "))
# print(salary)
# salary_int = int(salary)
# print(salary_int)

# print(type(salary))

# a = 10
# b = 20
# print(a)
# print(b)
# arithmetic way
# a = a + 10
# b = b - 10
# print(a)
# print(b)
# tuple unpacking method 
# a,b = b,a
# print(a)
# print(b)

# a = '100'
# b = int(a) + 50
# print(b)

# l1 = [1,2,3,4,5,6,7,8,9,10,10,1]
# print(max(l1)) #max function for print largest element in list

# print(sum(l1)) #sum function for print total sum of elements in list

# print(set(l1)) #direct by typecast , set(list) but it may be or may not be maintain order

# print(l1.count(10)) #list.count(element) for print count how many times element appear in list

# l2 = [2]
# number = int(input("enter number : "))
# if(number % 2 == 0):
#     l2.append(number) #list.append(number) then it is added to the list
#     print(f"number is even ,number - {number} and list - {l2}")
# else :
#     print(f"number is not even ,number - {number} and list - {l2}")

# t1 = (1,2,3,4,5)
# print(t1[4])         #tuple is indexable that's why it is easy way to print

# print(t1.count(1))   #tuple.count(element) is same as list funtion 

# l1 = list(t1)     #direct possible tuple to list by typecast , list = list(tuple)
# print(l1)
# print(type(l1))

# print(len(t1))   #length function , len(tuple) and len(list) in both it worked

# print(1 in t1)  #in operator to check element , it gives false and true

# num = 1
# while(num < 101):
#     print(num)
#     num = num + 1

# while(num < 101):
#     if(num % 2 == 0):
#         print(num)
#     num = num + 1

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# num = 7
# print("Multiplication Table of 7")
# for i in range(1,11):
#     print(f"7 * {i} = {num*i}")
#     i = i + 1

# l1 = [1,2,3,4,5,6,7,8,9]
# count = 0
# for i in l1:
#     if(i > 5):
#         count = count + 1
# print(f"{count} numbers are greater than 5 in list")

# def square(num):
#     num = num ** 2
#     return num
# number = int(input("enter your number : "))
# print(square(number))

# def even__odd(num):
#     if(num % 2 == 0):
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
# even__odd(number)

# def max_no_list(list):
#     print(max(list))
# l1 = [1,2,3,4,5]
# max_no_list(l1)

# def return_sum(num1,num2):
#     sum = num1 + num2
#     return sum
# a = 10
# b = 20
# print(return_sum(a,b))

# def counts_list(list):
#     print(len(list))
# l1 = [1,2,3,4,5,6]
# counts_list(l1)

# content = "Shreyam is close range player. \nHe is using awm always. \n" \
# "He is good in sniper but because of that , lack of rushing in his gameplay. \n" \
# "He is an old player. \nAt last i say that he is good and average player."
# with open("file.txt","w") as f:
#     f.write(content)

# with open("file.txt") as f:
#     a = f.readlines()
#     print(len(a))

# with open("file.txt") as f:
#     a = f.read()
#     b = a.count("Python")
#     print(b)

#single line numbers without spaces 
#single line numbers with spaces
# with open("file.txt") as f:
#     number = f.read() #f.read().split() for remove spaces
#     count = 0
#     for i in number:
#         count = count + int(i)
#     print(count)

#multiple line numbers without spaces and with spaces but single number 
'''1 
2  right 

1 2 wrong
3'''
# with open("file.txt") as f:
#     number = f.readlines()
#     sum = 0
#     for line in number:
#         sum += int(line)
#     print(sum)

# with open("file.txt") as f:
#     content = f.read()
# with open("copy.txt","w") as c:
#     c.write(content)



