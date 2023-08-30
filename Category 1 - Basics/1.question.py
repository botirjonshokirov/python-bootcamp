# Print the result of the multiplication of two sets of integers if it is less than 1000. If the result is greater that 1000, print their sum.

# num1 = 25
# num2 = 26


num1 = 35
num2 = 36


def multiplication_or_sum(num1, num2):
    if (num1 * num2 > 1000):
        return num1 + num2
    return num1 * num2


print(multiplication_or_sum(num1, num2))
