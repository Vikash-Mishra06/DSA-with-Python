#Q1. Print Stars Pattern
# *
# **
# ***
# ****

# for i in range(1, 5):
#     print("*" * i)

#----------------------------------------------------------------------------------

#Q2. Print Number pattern

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

#----------------------------------------------------------------------------------

#Q3. Reverse a string

# def reverse_string(str):
#     return str[:: -1]
# print(reverse_string("Vikash"))

#----------------------------------------------------------------------------------

#Q4. Check palindrome

# def check_palindrome(str):
#     return str == str[:: -1]
# print(check_palindrome("madam"))

#----------------------------------------------------------------------------------

#Q5. Count vowels

# def count_vowels(str):
#     count = 0
#     for ch in str.lower():
#         if ch in "aeiou":
#             count += 1
#     return count
# print(count_vowels("Javascript"))

#----------------------------------------------------------------------------------

# Q6. Find Maximum in List

# arr = [3, 7, 2, 9]
# max_value = arr[0]
# for num in arr:
#     if num > max_value:
#         max_value = num
# print(max_value)

#----------------------------------------------------------------------------------

# Q7. Remove Duplicates

# arr = [1,1,2,2,3,3,4,4]
# print(list(set(arr)))

#----------------------------------------------------------------------------------

# Q8. Fibonacci Series

# a, b = 0, 1
# for i in range(5):
#     print(a, end=" ")
#     a, b = b, a+b

#----------------------------------------------------------------------------------

# Q9. Prime Number

# n = 7
# is_prime = True
# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False
#         break
# print(is_prime)
