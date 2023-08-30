# Reverse a given number and return true if it is the same as the original number

num1 = 323

num2 = 625


def reversed_num(num):
    original_number = num
    reversed_num = 0

    while (num > 0):
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
    if original_number == reversed_num:
        return True
    else:
        return False


print(reversed_num(num2))
