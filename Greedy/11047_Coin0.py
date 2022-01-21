# K원을 만들기 위해 최소한으로 필요한 동전 갯수
import sys

def MinNumCoin(valuelist, K):
    if K == 0:
        return 0

    for i in range(len(valuelist)):
        q = K // valuelist[-(i+1)]
        if q != 0:
            restK = K % valuelist[-(i+1)]
            rslt = MinNumCoin(valuelist[:-(i+1)], restK)
            return q + rslt


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    CoinValue = []
    result = 0
    for _ in range(N):
        CoinValue.append(int(input()))

    answer = MinNumCoin(CoinValue, K)
    print(answer)