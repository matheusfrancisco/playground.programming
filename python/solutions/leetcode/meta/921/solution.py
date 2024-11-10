class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            elif not stack:
                moves += 1
            elif c == ")" and stack[-1] == "(":
                stack.pop()
        return moves + len(stack)

def minAddToMakeValid(s: str) -> int:

    open = 0
    minr = 0
    for char in s:
        if char == "(":
            open += 1
        else:
            if open > 0:
                open -= 1
            else:
                minr += 1
    return minr + open
