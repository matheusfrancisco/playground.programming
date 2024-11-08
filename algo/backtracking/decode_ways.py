
"""
We have a message consisting of digits 0-9 to decode. Letters are encoded to digits by their positions in the alphabet

A -> 1
B -> 2
C -> 3
...
Y -> 25
Z -> 26
Given a non-empty string of digits, how many ways are there to decode it?

Input: "18"

Output: 2

Explanation: "18" can be decoded as "AH" or "R"

Input: "123"

Output: 3

Explanation: "123" can be decoded as "ABC", "LC", "AW"
Time complexity
The time complexity of the memoization solution is the size of the memo 
array O(n) multiplied by the number of operations per state which is O(1).
So the overall time complexity is O(n).

Space complexity
The height of the state-space tree is at most O(n). 
The size of the memo array is O(n). Therefore the space complexity is O(n).
"""

def decode_ways(digits: str) -> int:
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]
        if start == len(digits):
            return 1
        ways = 0
        if digits[start] == "0":
            return ways
        ways += dfs(start + 1)
        if 10 <= int(digits[start:start + 2]) <= 26:
            ways += dfs(start + 2)
        memo[start] = ways
        return ways

    return dfs(0)


print(decode_ways("12"))  # 2
# (out) 2
