import sys
import itertools # 파이썬 조합 라이브러리 (built-in 라이브러리임)
import math # math.inf 쓰려고 

if __name__=='__main__':
    N, M = map(int, input().split())
    HouseCoord = []
    ChickCoord = []
    for i in range(N):
        layer = list(map(int, sys.stdin.readline().split()))
        while 1 in layer:
            Hidx = layer.index(1)
            HouseCoord.append([i, Hidx])
            layer[Hidx] = 0
        
        while 2 in layer:
            Cidx = layer.index(2)
            ChickCoord.append([i, Cidx])
            layer[Cidx] = 0

    ChickNum = len(ChickCoord) # 지도에 있는 전체 치킨집 갯수
    ChickDist = []
    for r1, c1 in HouseCoord:
        DistTemp = []
        for r2, c2 in ChickCoord:
            DistTemp.append(abs(r1-r2)+abs(c1-c2))
        ChickDist.append(DistTemp)
    
    MinDist = math.inf
    NumOfCase = list(itertools.combinations(range(ChickNum), M))
    for case in NumOfCase:
        CityDist = 0
        for dist in ChickDist:
            CityDist += min([dist[x] for x in case])
        
        if CityDist < MinDist:
            MinDist = CityDist

    print(MinDist)