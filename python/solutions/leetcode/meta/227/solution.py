

# this have an edge cases 333 + 3 * 3
# you have to remember to parse the value 333

# 
# 0 * 10 + 3 = 3
# 3 * 10 + 3 = 33
# 33 * 10 + 3 = 333


def calculate(s):

    i = 0
    cur = prev = res = 0
    cur_operation = "+"

    while i < len(s):
        cur_c = s[i]

        if cur_c.isdigit():
            while i < len(s) and s[i].isdigit():
                cur = cur * 10 + int(s[i])
                i += 1

            i -= 1

            if cur_operation == "+":
                res += cur
                prev = cur

            elif cur_operation == "-":
                res -= cur
                prev = -cur

            elif cur_operation == "*":

                res -= prev
                res += prev * cur
                prev = cur * prev
            else:
                res -= prev
                res += int(prev / cur)
                prev = int(prev / cur)
            cur = 0
        elif cur_c != " ":

            cur_operation = cur_c
        i += 1

    return res


s = "3+2*2"
r = calculate(s)
assert r == 7
