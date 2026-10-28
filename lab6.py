import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
jobs = sorted(zip(data[1::2], data[2::2]))
busy = []
answer = 0
for start, duration in jobs:
    while busy and busy[0] <= start:
        heapq.heappop(busy)
    heapq.heappush(busy, start + duration)
    answer = max(answer, len(busy))
print(answer)
