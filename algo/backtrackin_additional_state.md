# Backtracking - Additional States


## Additional constraints

In Palindrome Partitioning, we had the constraints that each part of the
partition must be a palindrome. We solved it by checking the validity of a
prefix before branching out. In some cases, the constraints are more imposed
by the problem require us to keep additional states to check the validity of
a branch


```python 
ans = []
def dfs(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()

```


