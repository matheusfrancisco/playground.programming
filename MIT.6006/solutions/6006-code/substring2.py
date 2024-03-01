def longest_substring(s, t):
    """Finds the longest substring that occurs in both s and t"""
    best = ''
    for length in range(min(len(s),len(t))+1):
        ans = k_substring(s, t, length)
        if ans is None:
            return best
        best = ans
    return best

def k_substring(s, t, k):
    """Finds a substring of length k in both s and t if there is one,
    and returns it. Otherwise, returns None."""
    s_substrings = set()
    # Put all substrings of s of length k into a set: s_substrings
    for s_start in range(len(s)-k+1):
        current = s[s_start : s_start+k]
        s_substrings.add(current)
    # For every substring of t of length k, look for it in
    # s_substrings. If it's there, return it.
    for t_start in range(len(t)-k+1):
        current = t[t_start : t_start+k]
        if current in s_substrings:
            return current
    return None
