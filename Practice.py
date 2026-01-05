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