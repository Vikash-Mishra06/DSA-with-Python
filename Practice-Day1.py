# Q.1) Print Star Pattern.

    # for i in range(5, 0, -1):
    #     print('*'*i)

    # Output:
    # *****
    # ****
    # ***
    # **
    # *
    
# Q.2) Print Number Pattern.

    # for i in range(5, 0, -1):
    #     for j in range(i, 0, -1):
    #         print(j, end='')
    #     print()
    
    # Output:
    # 54321
    # 4321
    # 321
    # 21
    # 1
    
# Q3) Reverse a string.

    # def reverse(str):
    #     return str[:: -1]
    # print(reverse('Vikash'))

    # Output: hsakiV

# Q4) Check palindrome.

    # def check_palindrome(str):
    #     return str == str[:: -1]
    # print(check_palindrome('madam'))
    
    # Output: True
    
# Q.5) Count vowels.

    # def count_vowels(str):
    #     vowels = 'aeiou'
    #     count = 0

    #     for ch in str.lower():
    #         if ch in vowels:
    #             count = count + 1
    #     return count
    # print(count_vowels("JavAScript"))
    
    # Output: 3
    
# Q6. Find Maximum in List

    # arr = [3, 7, 2, 9]
    # max_val = arr[0]
    # for num in arr:
    #     if num > max_val:
    #         max_val = num
    # print(max_val)

    # Output: 9

# Q7. Remove Duplicates

    # arr = [1,2,2,3,4,4]
    # print(list(set(arr)))
    
    # Output: [1, 2, 3, 4]
    
# Q8. Fibonacci Series

    # a, b = 0, 1
    # for i in range(5):
    #     print(a, end=" ")
    #     a, b = b, a+b
    
    # Output: 0 1 1 2 3 

# Q9. Prime Number

    # n = 7
    # is_prime = True
    # for i in range(2,n):
    #     if n % i == 0:
    #         is_prime = False
    #         break
    # print(is_prime)
    
    # Output: True

# Q10. Character Frequency

    # s = "apple"
    # freq = {}
    # for ch in s:
    #     freq[ch] = freq.get(ch,0) + 1
    # print(freq)

    # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    
# Q11. Sum of Array

    # arr = [1,2,3,4]
    # total = 0
    # for num in arr:
    #     total += num
    # print(total)

    # Output: 10