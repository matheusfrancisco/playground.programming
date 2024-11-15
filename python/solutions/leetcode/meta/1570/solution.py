from typing import List

class SparseVector1:
    def __init__(self, nums: List[int]):
        self.values = {}
        for idx in range(len(nums)):
            n = nums[idx]
            if n > 0:
                self.values[idx] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector1') -> int:
        product = 0
        for k, v in self.values.items():
            if k in vec.values:
                product += v * vec.values[k]

        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = [(idx, nums[idx]) for idx in range(len(nums)) if nums[idx] > 0]

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        vec1 = 0
        vec2 = 0

        while vec1 < len(self.values) and vec2 < len(vec.values):
            idx1, n1 = self.values[vec1]
            idx2, n2 = vec.values[vec2]
            if idx1 == idx2:
                product += n1 * n2
                vec1 += 1
                vec2 += 1
            elif idx1 > idx2:
                vec2 += 1
            else:
                vec1 += 1
        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
