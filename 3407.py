import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
population = data[1:]
events = [(max(1000 - f, 1), i) for i, f in enumerate(population)]
heapq.heapify(events)
time = 0
position = 0
while True:
    birth, aquarium = heapq.heappop(events)
    if abs(aquarium - position) > birth - time:
        print(birth)
        break
    time, position = birth, aquarium
    population[aquarium] += 1
    heapq.heappush(events, (birth + max(1000 - population[aquarium], 1), aquarium))
