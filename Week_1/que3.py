import string

word = "#2a$#b%c%561#"


def replace_digits(word):
    str_new = []
    for i in word:
        if i in string.digits: str_new.append("#")
    return "".join(str_new)


new_string = replace_digits(word)
print(new_string)
