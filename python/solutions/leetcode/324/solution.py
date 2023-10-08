
def is_power_of_four(n):
    return ((n > 0) and ((n & n - 1) == 0) and (n % 3 == 1))


def main():
    n = int(input())
    for i in range(n):
        print(is_power_of_four(int(input())))

main()
