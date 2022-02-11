import sys
from collections import deque

S = sys.stdin.readline().strip()
T = deque(sys.stdin.readline().strip())

revFlag = False
while True:
    if len(S) == len(T):
        break

    if revFlag:
        obj = T.popleft()
        if obj == 'B':
            revFlag = not revFlag
        continue

    obj = T.pop()
    if obj == 'B':
        revFlag = not revFlag

if revFlag:
    T.reverse()
print(1 if S == ''.join(T) else 0)