#  Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def remove_string(str, num):
    return str[num:]


name = "Botirjon"
print(remove_string(name, 2))
