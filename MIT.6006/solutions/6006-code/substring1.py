def longest_substring(s, t):
    """Finds the longest substring that occurs in both s and t"""
    best = ''
    for s_start in range(0, len(s)):
        for s_end in range(s_start, len(s)+1):
            for t_start in range(0, len(t)):
                for t_end in range(t_start, len(t)+1):
                    if s[s_start:s_end] == t[t_start:t_end]:
                        current = s[s_start:s_end]
                        if len(current) > len(best):
                            best = current
    return best
