from typing import List
import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email_to_account = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                print(email, acc[1])
                graph[email].add(acc[1])
                graph[acc[1]].add(email)
                email_to_account[email] = name

        res = []
        visited = set()

        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                local_res = []
                while stack:
                    node = stack.pop()
                    local_res.append(node)
                    for edge in graph[node]:
                        if edge not in visited:
                            stack.append(edge)
                            visited.add(edge)
                res.append([email_to_account[email]] + sorted(local_res))
        return res


acc = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                                 "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
print(Solution().accountsMerge(acc))

# O(N*K*NlogK) N is the number of accounts, 
# K is the average number of emails in each account

# Space complexity: O(N*K) N is the number of accounts,
