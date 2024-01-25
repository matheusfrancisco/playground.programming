def sum_of_three(nums, target):
    nums.sort()
    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == target:
                return True
            elif tmp < target:
                j += 1
            else:
                k -= 1
        return False

assert(sum_of_three([1,2,3,4,5], 6) == True)
