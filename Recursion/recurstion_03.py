def sum_of_number(n):
    if n == 0:
        return 0
    else:
        return  sum_of_number(n-1) + n
        
print(sum_of_number(5))


def is_palindrome_math(num):
    # Negative numbers cannot be palindromes
    if num < 0:
        return False

    original = num
    reversed_num = 0

    # Reconstruct the number in reverse
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    # Check if the reversed number matches the original
    return original == reversed_num


# Test cases
print(is_palindrome_math(1331))  # Returns: True
print(is_palindrome_math(1234))



num = 1331

if num < 0:
    print("Number was nagtive")
orignal = num
rever_num = 0

while num > 0:
    d = num % 10
    rever_num = (rever_num * 10) + d
    num //= 10

print(orignal)
print(rever_num)
if orignal == rever_num:

    print("Number was palindrome")
else:
    print("Number was not palindrome")
