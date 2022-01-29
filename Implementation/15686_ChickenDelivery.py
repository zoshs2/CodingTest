import sys

if __name__=='__main__':
    N, M = map(int, input().split())
    layers = []
    NumHouse = 0
    for i in range(N):
        layers.append(list(map(int, sys.stdin.readline().split())))
        if 1 in layers[i]:
            NumHouse += layers[i].count(1)

    print(NumHouse)
    
    