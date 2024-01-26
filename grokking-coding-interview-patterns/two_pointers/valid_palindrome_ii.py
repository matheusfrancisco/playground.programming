

# remove at most one character to make it a palindrome

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True

def valid_palindrome_ii(s):
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return is_palindrome(s, start + 1, end) or is_palindrome(s, start, end - 1)
        start += 1
        end -= 1
    return True

print(valid_palindrome_ii("abceba"))
#true

assert(valid_palindrome_ii("abceba") == True)

