# Backtracking Aggregation

All the backtracking problems we have seen so far ask us to generate all 
the combinations of things. For example, generating all combinations or 
permutations of letters, generating all valid parentheses and generating 
all valid palindrome partitions.

In this section, we will look at problems that ask questions such as

Is it possible to make up a word using other words from a dictionary?
Find the number of ways to decode a message
Find the minimum number of coins to make up an amount
We categorize these "aggregation" problems because we aggregate the return value from child recursive calls to parent and bubble them up. It's very similar to how Max Depth of a Tree and Visible Tree Node aggregate return values.


```python
def dfs(start_index, [...additional states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [...additional states]):
        if additional states: 
            update([...additional states])
        ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
        if additional states: 
            revert([...additional states])
    return ans
```

The main differences between this and the previous template are:

no path and push/pop since we don't need to actually generate the solutions. 
We just need the aggregated value.
use return value to aggregate results from child dfs calls.
Depending on what the problem asks for, the initial_value and aggregate function here can be

Problem statement:
    If it's possible? does it exist?
intial_value:
    False
aggregate:
    logical OR (||)


Problem statement:
    Number of ways to...
intial_value:
    0
aggregate:
    sum/+

Problem statement:
    Minimum/maximum ways/value to...
intial_value:
    inf/max
aggregate:
    min/max

We will go through a couple of concrete problems in the following 
articles. Before that, let's introduce one more useful technique that is 
often used in backtracking aggregation problems.

