# Write code to extract each digit from the integer, in the reverse order

integer = 33154689

while (integer > 0):
    digit = integer % 10
    print(digit)
    integer = integer // 10
