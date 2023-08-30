# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

list = [10, 20, 33, 46, 55, 77, 105, 204, 335]


def divisible_five(list):
    for num in list:
        if (num % 5 == 0):
            print(num)


print(divisible_five(list))
