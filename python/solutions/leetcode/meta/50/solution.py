class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = n < 0
        n = abs(n)

        self.mem = {}
        res = self.fast_pow(x, n)
        return 1/res if is_neg else res

    # 2^5 = 2^2 * 2^2 * 2
    # 2^6 = 2^3 * 2^3 -> 
    # first part 2^2 * 2^1 = 2^3
    # second part 2^2 * 2^1 = 2^3
    # it will alreay be calculated and it will be stored in the mem
    # 2^7 = 2^3 * 2^3 * 2
    def fast_pow(self, x, n):
        if n in self.mem:
            return self.mem[n]
        if n == 0:
            return 1
        elif n == 1:
            return x
        self.mem[n] = self.fast_pow(x, n//2) * self.fast_pow(x, n//2) * (x if n % 2 else 1)
        return self.mem[n]
# T: O(logn)
# S: O(logn)
