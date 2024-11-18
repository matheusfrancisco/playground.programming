import collections
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        meeting_dict = collections.defaultdict(list)

        for p1, p2, time in meetings:
            meeting_dict[time].append([p1, p2])

        has_secret = {0, firstPerson}

        for time, meets in meeting_dict.items():

            graph = collections.defaultdict(list)
            seen = set()

            for p1, p2 in meets:
                graph[p1].append(p2)
                graph[p2].append(p1)

                if p1 in has_secret:
                    seen.add(p1)

                if p2 in has_secret:
                    seen.add(p2)

            queue = collections.deque(seen)

            while queue:
                p = queue.popleft()

                for neighbor in graph[p]:
                    if neighbor not in has_secret:
                        has_secret.add(neighbor)

                        queue.append(neighbor)
        # T O(NlogN) * O(N) + O(N)
        # S O(N) + O(N) + O(N)
        return list(has_secret)
