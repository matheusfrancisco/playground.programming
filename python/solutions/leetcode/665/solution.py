

def check_possibility(nums: list[int]) -> bool:
    if len(nums) == 0:
        return True
    if len(nums) == 1:
        return True
    
    changed = False
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if changed:
            return False
        if i == 0 or nums[i - 1] <= nums[i + 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        changed = True

    return True

assert check_possibility([2, 3]) == True

def main():
    n = int(input())
    for i in range(n):
        nums = list(map(int, input().split(" ")))
        out = check_possibility(nums)
        print(out)

main()
