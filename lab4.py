import sys
import heapq

heap = []
out = []
for line in sys.stdin.buffer:
    command = line.split()
    if not command:
        continue
    if command[0] == b"CLEAR":
        heap.clear()
    elif command[0] == b"ADD":
        heapq.heappush(heap, -int(command[1]))
    else:
        out.append(str(-heapq.heappop(heap)) if heap else "CANNOT")
sys.stdout.write("\n".join(out))
