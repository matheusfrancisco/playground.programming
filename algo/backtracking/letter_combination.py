from typing import List

# Given a non-negative integer n, find all n-letter words
# composed by 'a' and 'b', return them in a list of
# strings in lexicographical order.

def letter_combination(n) -> List[int]:
    res: List[str] = []

    def dfs(start_index: int, path: List[str]) -> None:
        if start_index == n:
            res.append("".join(path))
            return
        for letter in "ab":
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res

# for each node there are a maximum of 2 children
# the height of the tree is n
# The number of nodes is 2^n-1 or O(2^n), (see the perfect binary tree)
# it takes O(n) to join n characters at each leaf node. So the overall
# time compexity is O(n*2^n)


# We store 2^n strings in total, each with a length of n so this gives us O(2^n*n) space. 
# In addition, our recursion depth is O(n). Adding the two together, we still get a space 
# complexity of O(2^n*n).


print(letter_combination(2) == ["aa", "ab", "ba", "bb"])
