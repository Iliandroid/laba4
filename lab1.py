import sys

def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    heap = []
    out = []
    for _ in range(n):
        if next(data) == 0:
            x = next(data)
            heap.append(x)
            i = len(heap) - 1
            while i and heap[(i - 1) // 2] < x:
                p = (i - 1) // 2
                heap[i] = heap[p]
                i = p
            heap[i] = x
        else:
            out.append(str(heap[0]))
            x = heap.pop()
            if heap:
                i = 0
                while 2 * i + 1 < len(heap):
                    j = 2 * i + 1
                    if j + 1 < len(heap) and heap[j + 1] > heap[j]:
                        j += 1
                    if heap[j] <= x:
                        break
                    heap[i] = heap[j]
                    i = j
                heap[i] = x
    print("\n".join(out))

if __name__ == "__main__":
    main()
