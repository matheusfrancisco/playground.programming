from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        carry = 1

        while i >= 0:
            cur = digits[i] + carry
            digits[i] = cur % 10
            carry = cur // 10
            if not carry:
                break
            i -= 1

        if carry:
            digits.insert(0, carry)
        return digits
# T: O(N)
# S: O(1)
