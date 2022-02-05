import sys

N, M = map(int, input().split())
cardList = list(map(int, sys.stdin.readline().strip().split()))
for _ in range(M):
    cardList = sorted(cardList)
    update = cardList[0] + cardList[1]
    cardList[:2] = [update] * 2

print(sum(cardList))