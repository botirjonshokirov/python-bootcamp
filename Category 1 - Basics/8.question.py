# Print the following pattern

"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

for num in range(6):
    for num2 in range(num):
        print(num, end="  ")
    print("\n")
