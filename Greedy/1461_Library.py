import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))
if N <= M:
    print(max(arr))
    exit(0)

rest = arr[:-M]
last_step = max(arr[-M:])

