import sys


prime_list = [False, False] + [True] * (N-1)
# N=10인 1부터 10사이의 자연수를 검사한다고 할 때, 2부터 모든 수가 소수(True)라고 가정하면 되기 때문에, 앞서 idx 0과 1을 포함해 N-1개만 더 만들면 된다.
# e.g. N=5라고 할때, 5개만 만드는게 아니라 결과적으로 (0 포함할 거니까) 6개(N+1)를 만들어야 한다. 근데 앞서 2개(0과, 1은 소수가 아님)가 False로 사전정의되어 있기에 N+1-2 = N-1 를 더 만든다는 얘기다.
# index 0과 1은 소수가 아닐테니 False, 그 외 나머지 값들은 모두 소수라고 가정한다.
cnt = 0
for i in range(N+1):
    if prime_list[i]: # False(소수가 아닌 것)들은 count에서 제외한다.
        cnt += 1
        for j in range(i+i, N+1, i): # e.g. i가 2라면, 4부터 시작해서 i의 배수들을 False로 바꿔 지워나간다.
            prime_list[j] = False
        
print(cnt)

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline())
