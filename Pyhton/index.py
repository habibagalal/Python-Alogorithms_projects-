# from bs4 import BeautifulSoup
# import requests
# import csv
# from itertools import zip_longest
# # fetch the url
# result = requests.git("https://wuzzuf.net/explore")
# # save the page content
# src = result.content

# # create soup object to parse content
# soup = BeautifulSoup(src, "lxml")
# print(soup)


# def binary(list, target):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (high + low) / 2
#         guess = list[mid]
#         if guess == target:
#             return mid
#         if guess < target:
#             low = mid + 1
#         else:
#             high = mid-1
#     return None


# print(binary([1, 2, 3, 4], 2))
num1 = float(input("please Enter Your First Number "))
operator = input("please Enter Your First Operator ")
num2 = float(input("please Enter Your First Operator "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Wrong Operator ")
