
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][0:i]
    return ""

def common_prefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[0:i]

def lcp_divide_and_conquer_helper(strs, l, r):
    if l == r:
        return strs[l]
    else:
        mid = (l + r) // 2
        lcp_left = lcp_divide_and_conquer_helper(strs, l, mid)
        lcp_right = lcp_divide_and_conquer_helper(strs, mid + 1, r)
        return common_prefix(lcp_left, lcp_right)

def lcp_divide_and_conquer(strs):
    if len(strs) == 0:
        return ""
    return lcp_divide_and_conquer_helper(strs, 0, len(strs) - 1)


def main():
    n = int(input())
    for i in range(n):
        strs = input().split(" ")
        out = lcp_divide_and_conquer(strs)
        print(f"{out}")

main()
