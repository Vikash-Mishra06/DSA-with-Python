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
    
