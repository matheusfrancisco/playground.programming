
## Backtracking Template

Combinatorial search problems involve finding groupings and assignments of 
objects that satisfy certain conditions. Finding all permutations, combinations,
subsets, and solving Sudoku are classic combinatorial problems. 
The time complexity of combinatorial problems often grows rapidly with the size 
of the problem. Feel free to go back to the math basics section for a review.

In combinatorial search problems, the search space (a fancy way of saying all 
the possibilities to search) is in the shape of a tree. The tree that represents 
all the possible states is called a state-space tree (because it represents all 
the possible states in the search space).

Each node of the state-space tree represents a state we can reach in a combinatorial 
search (by making a particular combination). Leaf nodes are the solutions to the 
problem. Solving combinatorial search problems boils down to DFS on 
the state-space tree. Since the search space can be quite large, we often have to 
"prune" the tree, i.e. discard branches and stop further traversals. 
This is why it's often called backtracking.

### Difference between previous DFS problems and backtracking

If you had followed the content in order, you would have gone through quite 
a few DFS-on-tree problems. The main difference between those problems and 
the backtracking problems is that in backtracking, we are not given a tree to 
traverse but rather we construct the tree/ generate the edges and tree nodes 
as we go. 
At each step of a backtracking algorithm, we write logic to find the edges 
and child nodes. This may sound abstract but I promise it’ll be much clearer 
once we start seeing a couple of problems.

1. how do we know if we have reached a solution?
2. how do we branch (generate the possible children)?
```python
defn dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
        return
    for edge in get_edges(start_index):
        path.add(edge)
        dfs(start_index + 1, path)
        path.pop()
```
`start_index` is used to keep track of the current level of the state-space tree
we are in.

`edge` is the choice we make; the string a, b in the above state-space trees.
the main logic we have to fill out is 
1. `is_leaf`
2. `get_edges`
which correspond to the two questions above

Notice how very similar this is to the Ternary Tree Path code. 

### Time and space complexity

We visit each node of the state apce tree excatly once, so the time complexity of a
backtracking algorithm is proportional to the number of nodes in the state-space tree.
The number of nodes in a tree can be calculated by multiplying `number of children of each node ^ height of the
tree`

The space complexity of a backtracking algorithm is typically the height of the tree
beacuse that's where the DFS recursive call stack is of maximum height of the tree beacuse
thet's where the DFS recurive call stack is of max height.


