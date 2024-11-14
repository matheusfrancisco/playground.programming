class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append((char, 1))
            else:
                if stack and stack[-1][0] == char:
                    char, d = stack.pop()
                    d += 1
                    if d < k:
                        stack.append((char, d))
                    elif d - k > 0:
                        stack.append((char, d-k))
                else:

                    stack.append((char, 1))
        s_out = ""
        for char, d in stack:
            s_out += char*d
        return s_out


print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
# "aa"
