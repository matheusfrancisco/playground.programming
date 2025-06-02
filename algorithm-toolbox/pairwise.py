from typing import List

def pairwise(iterable: List) -> int:

    first_max, second_max = float('-inf'), float('-inf')
    idx = 0
    
    for i, num in enumerate(iterable):
        if num > first_max:
            first_max = num
            idx = i

    for i, num in enumerate(iterable):
        if i != idx and num > second_max:
            second_max = num

    return first_max * second_max

n = int(input())

numbers = list(map(int, input().split()))

print(pairwise(numbers))  # Output: 20

