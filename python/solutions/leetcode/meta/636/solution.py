from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        execution = [0] * n
        call_stack = []
        prev_start_time = 0
# ["0:start:0","1:start:2","1:end:5","0:end:6"]
# 0 , start, 0
# prev = 0
# [0, ]
# prev = 0
# 1, start, 2
# [0, 1]
# [2, ]
# prev = 2
# 1 end 5
# [0,]
# . [2, 4]
# prev = 6
# [ 3, 4]
        for log in logs:
            func_id, call_type, timestamp = log.split(":")

            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if call_stack:
                    execution[call_stack[-1]] += timestamp - prev_start_time
                call_stack.append(func_id)
                prev_start_time = timestamp
            else:
                execution[call_stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1
        return execution
