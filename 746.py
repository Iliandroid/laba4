import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
heap = data[1:]
heapq.heapify(heap)
total = 0
while len(heap) > 1:
    value = heapq.heappop(heap) + heapq.heappop(heap)
    total += value
    heapq.heappush(heap, value)
cents = total * 5
print(f"{cents // 100}.{cents % 100:02d}")
