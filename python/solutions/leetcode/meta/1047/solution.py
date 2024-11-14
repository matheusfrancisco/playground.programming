
# we want remove the duplicates
# using a stack
# Input: s = "abbaca"

# Time is O(N)
# S: O(N)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))  # "ca"
