def findWinners( matches):
    losses = {}
    for i, j in matches:
        if i not in losses:
            losses[i] = 0
        if j not in losses:
            losses[j] = 0
        losses[i] += 0
        losses[j] += 1
    ans = [[], []]
    for k in losses.keys():
        if losses[k] <= 1:
            ans[losses[k]].append(k)
    ans[0].sort()
    ans[1].sort()
    return ans


def main():
    i = int(input())
    p = []
    for _ in range(i):
        k, v = input().split(" ")
        p.append([int(k),int(v)])
    print(findWinners(p))

main()
    
