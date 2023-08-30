# In a string, display the characters at the even indices

name = "Botirjon"


def even_char(str):
    for char in range(0, len(str), 2):
        print(str[char])


even_char(name)
