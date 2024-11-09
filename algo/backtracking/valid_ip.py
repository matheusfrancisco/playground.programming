
# template
# ans = []
# def dfs(start_index, path, [...additional states]):
#    if is_leaf(start_index):
#        ans.append(path[:]) # add a copy of the path to the result
#        return
#    for edge in get_edges(start_index, [...additional states]):
#        # prune if needed
#        if not is_valid(edge):
#            continue
#        path.add(edge)
#        if additional states:
#            update(...additional states)
#        dfs(start_index + len(edge), path, [...additional states])
#        # revert(...additional states) if necessary e.g. permutations
#        path.pop()

def valid_ip(s):
    res = []

    def is_valid(num):
        if num == "0":
            return True
        elif num[0] == "0":
            return False    # leading zero
        elif int(num) > 255:
            return False   # out of range
        else:
            return True

    def to_ip(path):
        adds = path[0]
        for i in range(1, 4):
            adds += '.' + path[i]
        return adds

    def get_edges(start):
        segments = []
        for i in range(start, start + 3):
            if i < len(s):
                segments.append(s[start:i + 1])
        return segments

    def dfs(start, path):
        if len(path) > 4:
            return
        if start == len(s):
            if len(path) == 4:
                res.append(to_ip(path))
            return

        for edge in get_edges(start):
            if is_valid(edge):
                path.append(edge)
                dfs(start + len(edge), path)
                path.pop()
    dfs(0, [])
    return res


print(valid_ip('2552552550'))
