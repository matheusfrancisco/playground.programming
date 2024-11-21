import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        l = r = 0
        t_counts = collections.Counter(t)

        matches = 0
        required_matches = len(t_counts)

        window_counts = collections.defaultdict(int)

        ans = (float("inf"), 0, 0)

        while r < len(s):
            cur_char = s[r]
            window_counts[cur_char] += 1

            if cur_char in t_counts and t_counts[cur_char] == window_counts[cur_char]:
                matches += 1

            while l <= r and matches == required_matches:
                to_remove = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r-l + 1, l, r)
                window_counts[to_remove] -= 1
                if to_remove in t_counts and t_counts[to_remove] > window_counts[to_remove]:
                    matches -= 1
                l += 1

            r += 1
        if ans[0] == float("inf"):
            return ""

        return s[ans[1]: ans[2] + 1]
