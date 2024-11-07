 ## Backtracking with Prunning


### What is pruning?

it literally means cutting branches off a tree.
In our case, we want to cut branches off our state-space tree. The fewer branches, the 
faster the algorithm runs.


### When do we want to prune a branch?

When it's clear that going into that branch would not yield a valid final stat.
This happens when the problem comes with one or more constraints, and the branches
violates those contraints.


```python

defn dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
        return
    for edge in get_edges(start_index):
        if not is_valid(edge):
            continue
        path.add(edge)
        dfs(start_index + len(edge), path)
        path.pop()

```
the differences are
* we added a pruning step that checks if a branch is valid using  `is_valid`
*  we increment `start_index` by variable size instead of always 1


