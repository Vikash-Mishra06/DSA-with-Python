# Q.1) Positive or Negative?

    # def check_number(num):
    #     if num > 0:
    #         return "Positive"
    #     elif num < 0:
    #         return "Negative"
    #     else:
    #         return "Zero"
        
    # print(check_number(2))   # Positive
    # print(check_number(0))   # Zero
    # print(check_number(-1))  # Negative

# ----------------------------------------------------------------------------

# Q.2) Even or Odd?

    # def check_even_odd(num):
    #     if num % 2 == 0:
    #         return "Even"
    #     else:
    #         return "Odd"
        
    # print(check_even_odd(2))  # Even
    # print(check_even_odd(1))  # Odd
    # print(check_even_odd(0))  # Even
    
# ----------------------------------------------------------------------------

# Q.3) Sum of First N Natural Number.

    # def check_number(num):
    #     sum = 0
        
    #     for i in range(1, num + 1):
    #         sum = sum + i
    #     return sum

    # print(check_number(5))   # 15
    
# ----------------------------------------------------------------------------

# Q.4) Sum of N natural numbers.

    # def check_numbers(num):
    #     sum = 0
        
    #     for i in range(1, num + 1):
    #         sum = sum + i
    #     return sum

    # print(check_numbers(5))   # 15
    
# ----------------------------------------------------------------------------

# Q.5) Sum of numbers in a given range.

    # def check_number(L, R):
    #     sum = 0
        
    #     for i in range(L, R + 1):
    #         sum = sum + i
    #     return sum

    # print(check_number(1, 5))   # 15
    
# ----------------------------------------------------------------------------

# Q.6) Greatest of two numbers.

    # def check_greatest(a, b):
    #     if a > b:
    #         return f"{a} is greater"
    #     elif b > a:
    #         return f"{b} is greater"
    #     else:
    #         return "Both are same"
        
    # print(check_greatest(10, 20))   # 20 is greater
    
# ----------------------------------------------------------------------------

# Q.7) Greatest of the Three numbers.

    # def greatest_of_three(a, b, c):
    #     if a > b and a > c:
    #         return f"{a} is greater"
    #     elif b > a and b > c:
    #         return f"{b} is greater"
    #     elif c > a and c > b:
    #         return f"{c} is greater"
    #     else:
    #         return "All are same"
        
    # print(greatest_of_three(10, 40, 30))   # 40 is greater

# ----------------------------------------------------------------------------

# Q.8) Leap year or not.

    # def check_leap_year(year):
        
    #     if year % 400 == 0:
    #         return f"{year} is a leap year"
    #     elif year % 100 == 0:
    #         return f"{year} is not a leap year"
    #     elif year % 4 == 0:
    #         return f"{year} is a leap year"
    #     else:
    #         return f"{year} is not a leap year"
        
    # print(check_leap_year(1300))  # Not a leap year
    
# ----------------------------------------------------------------------------

# Q.9) Prime number.

    # def is_prime(n):
    #         if n <= 1:
    #             return "Not Prime"

    #         for i in range(2, n):
    #             if n % i == 0:
    #                 return "Not Prime"
    #         return "Prime"
            
    # print(is_prime(41))  # Prime
    
# ----------------------------------------------------------------------------

# Q.10) Prime number within a given range.

    # def check_prime(n):
    #     if n <= 1:
    #         return False

    #     for i in range(2, n):
    #         if n % i == 0:
    #             return False
                
    #     return True

    # def primes_in_range(L, R):
    #     primes = []
            
    #     for num in range(L, R + 1):
    #         if check_prime(num):
    #             primes.append(num)
                    
    #     return primes

    # print(primes_in_range(1, 10))   # [2, 3, 5, 7]