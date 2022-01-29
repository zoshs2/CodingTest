import sys
import itertools # 파이썬 조합 라이브러리 (built-in 라이브러리임)

if __name__=='__main__':
    N, M = map(int, input().split())
    layers = []
    HouseCoord = []
    ChickCoord = []
    for i in range(N):
        layers.append(list(map(int, sys.stdin.readline().split())))
        while 1 in layers[i]:
            Hidx = layers[i].index(1)
            HouseCoord.append([i, Hidx])
            layers[i][Hidx] = 0
        
        while 2 in layers[i]:
            Cidx = layers[i].index(2)
            ChickCoord.append([i, Cidx])
            layers[i][Cidx] = 0

    ChickNum = len(ChickCoord)
    ChickDist = []
    for r1, c1 in HouseCoord:
        DistTemp = []
        for r2, c2 in ChickCoord:
            DistTemp.append(abs(r1-r2)+abs(c1-c2))
        ChickDist.append(DistTemp)
    
    MinDist = 0
    NumOfCase = list(itertools.combinations(range(ChickNum), M))

    
