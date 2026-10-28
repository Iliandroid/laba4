import sys

def sift(a, i, size):
    x = a[i]
    while 2 * i + 1 < size:
        j = 2 * i + 1
        if j + 1 < size and a[j + 1] > a[j]:
            j += 1
        if a[j] <= x:
            break
        a[i] = a[j]
        i = j
    a[i] = x

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]
    for i in range(n // 2 - 1, -1, -1):
        sift(a, i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift(a, 0, end)
    print(*a)

if __name__ == "__main__":
    main()
