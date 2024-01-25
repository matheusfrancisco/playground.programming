import re

def str_rev(_str, start, end):
    while start < end:
        temp = _str[start]
        _str[start] = _str[end]
        _str[end] = temp
        start += 1
        end -= 1

def reverse_string_1(string):
    
    s = re.sub(' +',' ',string.strip())
    s = list(s)
    str_len = len(s)

    str_rev(s, 0, len(s) - 1)
    start = 0
    end = 0
    while (start < str_len):
        while (end < str_len and s[end] != ' '):
            end += 1
        str_rev(s, start, end - 1)
        start = end + 1
        end += 1

    return "".join(s)

def invert(n, s, start, end):
    while end >= start:
        n += s[end]
        end -= 1

    return n 

def reverse_string(s):
    "not using extra space"
    s = re.sub(' +',' ',s.strip())
    s = s[::-1]
    start = 0
    end = 0
    str_len = len(s)

    n = ""
    while start < str_len:
        while (end < str_len and s[end] != " "):
            end += 1
        n = invert(n, s, start, end -1)
        start = end+ 1
        if start < str_len:
            n += " "
        end += 1
    return n

print(reverse_string("Hello World"))
# (out) World Hello
assert(reverse_string("Hello World") == "World Hello")
assert(reverse_string("Hello   World") == "World Hello")
assert(reverse_string_1("Hello   World") == "World Hello")

