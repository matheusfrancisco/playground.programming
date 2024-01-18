import collections

def close_strings(word1: str, word2: str) -> bool:
    f = collections.Counter(word1)
    f2 = collections.Counter(word2)
    s = sorted(f.values())
    s2 = sorted(f2.values())
    k = set(f.keys()) == set(f2.keys())
    return s == s2 and k

def main():
    w,w2 = input().split(" ")
    print(close_strings(w, w2))

main()

