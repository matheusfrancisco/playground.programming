# DFS

When you are apply DFS, when you are a node, the only things you know are:
1. Your value
2. Your children

```python
def dfs(node, state):
    if node is null:
        ...
        return

    left = dfs(node.left, state)
    right = dfs(node.right, state)

        ...

    return ...
```

1. Return value: 
