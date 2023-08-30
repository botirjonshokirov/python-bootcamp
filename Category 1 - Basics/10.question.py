# Given two list of numbers, create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]


def odd_even_numbers(list1, list2):
    list3 = []
    for nums in list1:
        if nums % 2 == 1:
            list3.append(nums)

    for nums in list2:
        if nums % 2 == 0:
            list3.append(nums)
    return list3


print(odd_even_numbers(list1, list2))
