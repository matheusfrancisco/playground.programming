import collections

def minSteps(s: str, t: str) -> int:
    c = collections.defaultdict(int)
    for i in range(len(s)):
        c[s[i]] += 1
        c[t[i]] -= 1
    out = 0
    for v in c.values():
        if v > 0:
            out += v
    
    return out


def main():
    s, t = input().split(" ")
    print(minSteps(s, t))

main()
