
def is_subsequence(s, t):
    left_t = 0
    left_s = 0
    while left_s < len(s) and left_t < len(t):
        if s[left_s] == t[left_t]:
            left_s += 1
        left_t += 1

    if left_s == len(s):
        return True
    return False

def main():
    n = int(input())
    for i in range(n):
        s, t = input().split(" ")
        out = is_subsequence(s, t)
        print(f"Output: {out}")

main()
