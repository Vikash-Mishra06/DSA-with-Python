# Q.1) Swapping Two Numbers

    # a = 10
    # b = 20
    # temp = a
    # a = b
    # b = temp
    # print(a, b)
    
    # OR
    
    # a = 10
    # b = 20
    # [a,b] = [b,a]
    # print(a, b)

# Q.2) Check Even or Odd Without Modulus

    # num = int(input("Enter a Number: "))
    # if num & 1 == 0:
    #     print("Even")
    # else:
    #     print("Odd")
    
    # OR
    
    # num = int(input("Enter a Number: "))
    # if num // 2 * 2 == num:
    #     print("Even")
    # else:
    #     print("Odd")
    
# Q.3) Check Even or Odd

    # def check_even_odd(num):
    #     if num % 2 == 0:
    #         return "Even"
    #     else:
    #         return "Odd"
    # print(check_even_odd(12))
    
# Q.4) Check Prime Number.

    # def check_prime(num):
    #     if num <= 1:
    #         return "Not a Prime Number"
    #     is_prime = True
        
    #     for i in range(2, int(num**0.5)+1):
    #         if num % i == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         return "Prime Number"
    #     else:
    #         return "Not a Prime Number"
            
    # print(check_prime(5))
    
# Q.5) Sum of Number.

    # def sum_of_number(num):
    #     sum = 0
        
    #     for i in range(1, num + 1):
    #         sum = sum + i
    #     return sum

    # print(sum_of_number(5))
    
# Q.6) Sum of numbers in a given range.

    # def sum_of_numbers(L, R):
    #     sum = 0
        
    #     for i in range(L, R+1):
    #         sum = sum + i
    #     return sum

    # print(sum_of_numbers(1, 5))
    
# Q.7 Check Perfect Number.

    # num = int(input("Enter a number: "))

    # if num <= 0:
    #     print("Not a Perfect Number")
    # else:
    #     total = 0
        
    #     for i in range(1, num // 2 + 1):
    #         if num % i == 0:
    #             total = total + i

    #     if total == num:
    #         print("Perfect Number")
    #     else:
    #         print("Not a Perfect Number")

# Q.8) Factorial Calculation – recursion.

    # def factorial(num):
    #     if num == 0 or num == 1:
    #         return 1
    #     else:
    #         return num * factorial(num -1)
        
    # num = int(input("Enter a number: "))

    # if num < 0:
    #     print("Factorial is not defined for negative numbers")
    # else:
    #     print("Factorial:", factorial(num))
    
# Q.9) Fibonacci Sequence.

    # n = int(input("Enter how many terms you want: "))

    # a, b = 0, 1

    # if n <= 0:
    #     print("Enter a Positive number")
    # elif n == 1:
    #     print(a)
    # else:
    #     print(a, b, end=" ")
        
    #     for _ in range(2, n):
    #         c = a + b
    #         print(c, end=" ")
    #         a = b
    #         b = c
    
# Q.10) GCD and LCM.

    # def gcd(a, b):
    #     while b != 0:
    #         a, b = b, a % b
    #     return a

    # def lcm(a, b):
    #     return (a*b) // gcd(a, b)

    # a = int(input("Enter first number: "))
    # b = int(input("Enter second number: "))

    # print("GCD:", gcd(a, b))
    # print("LCM:", lcm(a, b))