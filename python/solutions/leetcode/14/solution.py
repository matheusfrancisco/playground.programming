
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][0:i]
    return ""

def main():
    n = int(input())
    for i in range(n):
        strs = input().split(" ")
        out = longest_common_prefix(strs)
        print(f"{out}")

main()
