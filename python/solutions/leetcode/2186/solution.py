
def minSteps(s: str, t: str) -> int:
    #count = collections.Counter()
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    steps = 0
    for c2 in t:
        if c2 not in count:
            count[c2] = 0
        count[c2] -= 1
    for n in count.values():
        steps += abs(n)
    return steps

def main():
    s, t = input().split(" ")
    print(minSteps(s, t))


main()
