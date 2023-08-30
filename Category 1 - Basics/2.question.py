# Iterate from the start number to the end number of the first 10 numbers, and In each iteration print the sum of the current number with the previous number


def sum_prev(sum):
    previous_num = 0

    for number in range(sum):
        sum = previous_num + number
        print(
            f"Previous number: {previous_num}, current number: {number}, and sum: {sum}")

        previous_num = number


sum_prev(10)
