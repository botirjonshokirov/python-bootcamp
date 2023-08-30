#  Print multiplication table from 1 to 10

for num in range(1, 11):
    print("Table with:", num)
    for num2 in range(1, 11):
        print(f"{num} * {num2} = {num*num2}")
