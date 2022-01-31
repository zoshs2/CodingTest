A, B = map(int, input().split())

cnt = 1
while True:
    if B == A:
        break
    elif B < A: # 일단은 A보다는 커야한다.
        cnt = -1
        break

    units = list(str(B))[-1]
    if int(units) == 1:
        B = int("".join(list(str(B))[:-1]))
        cnt += 1
        continue
    elif B % 2 == 0:
        B = B//2
        cnt += 1
        continue
    else: # 중간에 앞선 두 경우에 맞는 케이스가 없다면, 무조건 글러먹은 조합이다. 따라서 -1 반환
        cnt = -1
        break

print(cnt)