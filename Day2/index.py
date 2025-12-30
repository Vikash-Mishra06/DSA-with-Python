# Q.1) Positive or Negative number.

    # def check_number(num):
    #     # Check if number is greater than 0
    #     if num > 0:
    #         return "Positive"
        
    #     # Check if number is less than 0
    #     elif num < 0:
    #         return "Negative"
        
    #     # If not greater and not less, it must be zero
    #     else:
    #         return "Zero"

    # print(check_number(5))    # Positive
    # print(check_number(-3))   # Negative
    # print(check_number(0))    # Zero

# ----------------------------------------------------------------------------

# Q.2) Even or Odd number.

    # def sum_of_n_numbers(n):
    #     total = 0  # this will store the sum
        
    #     # loop from 1 to n (inclusive)
    #     for i in range(1, n + 1):
    #         total += i   # add each number to total
        
    #     return total

    # print(sum_of_n_numbers(5))   # 15
    # print(sum_of_n_numbers(3))   # 6
    # print(sum_of_n_numbers(1))   # 1

# ----------------------------------------------------------------------------

# Q.3) Sum of First N Natural numbers.

    # def sum_of_n_numbers(n):
    #     total = 0  # this will store the sum
        
    #     # loop from 1 to n (inclusive)
    #     for i in range(1, n + 1):
    #         total += i   # add each number to total
        
    #     return total

    # print(sum_of_n_numbers(5))   # 15
    # print(sum_of_n_numbers(3))   # 6
    # print(sum_of_n_numbers(1))   # 1

# ----------------------------------------------------------------------------

# Q.4) Sum of N natural numbers.

    # def sum_of_n(n):
    #     total = 0   # start sum at 0

    #     # add every number from 1 to n
    #     for i in range(1, n + 1):
    #         total += i

    #     return total

    # print(sum_of_n(5))   # 15
    # print(sum_of_n(3))   # 6
    # print(sum_of_n(1))   # 1

# ----------------------------------------------------------------------------

# Q.5) Sum of numbers in a given range.

    # def sum_in_range(L, R):
    #     total = 0  # to store the sum

    #     # loop from L to R (inclusive)
    #     for num in range(L, R + 1):
    #         total += num  # add each number to total

    #     return total

    # print(sum_in_range(1, 5))   # 15
    # print(sum_in_range(3, 7))   # 25

# ----------------------------------------------------------------------------

# Q.6) Greatest of two numbers.

    # def greatest_of_two(a, b):
    #     # Check if a is greater than b
    #     if a > b:
    #         return f"{a} is greater"
        
    #     # Check if b is greater than a
    #     elif b > a:
    #         return f"{b} is greater"
        
    #     # If both are equal
    #     else:
    #         return "Both are equal"

    # print(greatest_of_two(5, 9))   # 9 is greater
    # print(greatest_of_two(10, 3))  # 10 is greater
    # print(greatest_of_two(4, 4))   # Both are equal

# ----------------------------------------------------------------------------

# Q.7) Greatest of the Three numbers.

    # def greatest_of_three(a, b, c):
    #     # Check if all are equal
    #     if a == b == c:
    #         return "All are equal"
        
    #     # Check if a is greatest
    #     if a > b and a > c:
    #         return f"{a} is greatest"
        
    #     # Check if b is greatest
    #     elif b > a and b > c:
    #         return f"{b} is greatest"
        
    #     # Otherwise c must be greatest (or tied with someone)
    #     else:
    #         return f"{c} is greatest"

    # print(greatest_of_three(5, 9, 2))    # 9 is greatest
    # print(greatest_of_three(10, 3, 8))   # 10 is greatest
    # print(greatest_of_three(4, 4, 4))    # All are equal
    
# ----------------------------------------------------------------------------

# Q.8) Leap year or not.

    # def is_leap_year(year):
    #     # Step 1: check divisible by 400
    #     if year % 400 == 0:
    #         return "Leap Year"
        
    #     # Step 2: check divisible by 100 (but not 400)
    #     elif year % 100 == 0:
    #         return "Not a Leap Year"
        
    #     # Step 3: check divisible by 4 (but not 100)
    #     elif year % 4 == 0:
    #         return "Leap Year"
        
    #     # Step 4: all other years are not leap years
    #     else:
    #         return "Not a Leap Year"

    # print(is_leap_year(2020))  # Leap Year
    # print(is_leap_year(2023))  # Not a Leap Year
    # print(is_leap_year(2000))  # Leap Year
    # print(is_leap_year(1900))  # Not a Leap Year

# ----------------------------------------------------------------------------

# Q.9) Prime number.

    # def is_prime(n):
    #     # 0, 1 and negative numbers are NOT prime
    #     if n <= 1:
    #         return "Not Prime"
        
    #     # check divisors from 2 to n-1
    #     for i in range(2, n):
    #         if n % i == 0:   # if divisible, not prime
    #             return "Not Prime"
        
    #     # if no divisor found, it's prime
    #     return "Prime"

    # print(is_prime(5))   # Prime
    # print(is_prime(6))   # Not Prime
    # print(is_prime(1))   # Not Prime
    # print(is_prime(2))   # Prime
    
# ----------------------------------------------------------------------------

# Q.10) Prime number within a given range.

    # def check_prime(n):
        # 0, 1 and negative numbers are NOT prime
    #     if n <= 1:
    #         return False
        
         # check divisors from 2 to n-1
    #     for i in range(2, n):
    #         if n % i == 0:  # divisible → not prime
    #             return False
            
    #     return True  # no divisors found → prime

    # def primes_in_range(L, R):
    #     primes = []
        
    #     for num in range(L, R + 1): # loop from L to R
    #         if check_prime(num):
    #             primes.append(num)
                
    #     return primes

    # print(primes_in_range(1, 10))   # [2, 3, 5, 7]
    # print(primes_in_range(10, 20))  # [11, 13, 17, 19]