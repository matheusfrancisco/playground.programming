
def climbing(n):
    """bottom up approach
    time : O(n)
    space : O(n)
    """
    m = [1, 1]
    t = 0
    for i in range(2,n+1):
        t = m[i-1] + m[i-2]
        m.append(t)
    return m[n]

def climbing_opt(n):
    """bottom up approach
    time : O(n)
    space : O(1)
    """
    first = 1
    second = 2
    for i in range(3,n+1):
        third = first+second
        first = second
        second = third
    return second

def main():
    n = int(input())
    for i in range(n):
        out = climbing_opt(int(input()))
        print(out)

main()
