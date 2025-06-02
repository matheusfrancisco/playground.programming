
def lcp(s1, s2):
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1[:min_len]


def lrs(s1):
    suffix = []
    for i in range(len(s1)):
        suffix.append(s1[i:])
    suffix.sort()
    longest = ""
    for i in range(len(suffix) - 1):
        lcp_value = lcp(suffix[i], suffix[i + 1])
        if len(lcp_value) > len(longest):
            longest = lcp_value
    return longest

print(lrs("bananaabcdekkkfdfsabcde"))
# Output: "abcde"

