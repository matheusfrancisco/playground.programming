

def simplifyPath(path):
    stack = []
    cur = ""

    for c in path + "/":
        if c == "/":
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += c

    return "/" + "/".join(stack)


simple_path = "/home///a/../b/c"

print(simplifyPath(simple_path))
print(simplifyPath(simple_path) == "/home/b/c")
