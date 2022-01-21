import sys

if __name__ == '__main__':
    n = int(input()) # The number of colleagues
    m = int(input()) # The number of relations
    relation = [False] + [False] * n
    visited = [False, True] + [False] * (n-1)
    for _ in range(m):
        n1, n2 = map(int, sys.stdin.readline().split())
        if not relation[n1]:
            relation[n1] = [n2]
        else:
            relation[n1].append(n2)

        if not relation[n2]:
            relation[n2] = [n1]
        else:
            relation[n2].append(n1)
    
    print(relation)
    if not relation[1]:
        print("0")
        sys.exit()
    
    for F in relation[1]: # Friend of 1
        visited[F] = True
        for FoF in relation[F]: # Friend of Friend(FoF)
            visited[FoF] = True
    
    answer = sum(visited) - 1 # Subtract by himself.
    print(answer)