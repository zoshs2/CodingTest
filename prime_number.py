
# 에라토스테네스의 체 - 알고리즘을 활용하여 소수를 찾아낸다.
# : 가장 대표적인 소수(Prime number) 판별 알고리즘.
# 대량의 숫자그룹에서 대량의 소수를 판별하려고 할 때 특히 효과적이다.
# 특정 숫자의 배수는 소수가 아니라는 법칙에서 착안된 방법. 
# 즉, 2~N의 배수들을 모두 제거하고, 제거되지 않은 숫자들을 소수로 판별하는 방식이다. 

# 소수란 자기 자신과 1을 제외한, 자기 자신보다 작은 두 자연수의 곱으로 만들 수 없는 자연수이다.

'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

입력 설명
-> 자연수의 개수(2<=N<=200,000)가 주어진다.

출력 설명
-> 소수의 개수를 출력한다.
'''

N = int(input("자연수의 개수(N)를 입력하세요 : "))

'''
prime_list = [False, False] + [True] * (N-1) 
# N=10인 1부터 10사이의 자연수를 검사한다고 할 때, 2부터 모든 수가 소수(True)라고 가정하면 되기 때문에, 앞서 idx 0과 1을 포함해 N-1개만 더 만들면 된다.
# e.g. N=5라고 할때, 5개만 만드는게 아니라 6개(N+1)를 만들어야 한다. 근데 앞서 2개가 False로 사전정의되어 있기에 N+1-2 = N-1 를 더 만든다는 얘기다.
# index 0과 1은 소수가 아닐테니 False, 그 외 나머지 값들은 모두 소수라고 가정한다.
cnt = 0

for i in range(N+1):
    if prime_list[i]: # False(소수가 아닌 것)들은 count에서 제외한다.
        cnt += 1
        for j in range(i+i, N+1, i): # e.g. i가 2라면, 4부터 시작해서 i의 배수들을 False로 바꿔 지워나간다.
            prime_list[j] = False
        
print(cnt)
'''

# 두 번째 version 
# Idea : 마찬가지로 해당 자연수 N까지의 리스트를 모두 소수라고 가정하고, 소수가 아닌 것들은 False로 바꿔주어 최종 True갯수들만 세면 된다.
# N=120까지를 검사한다고 할 때, 11^2 = 121 이므로 11까지만 배수들을 지우면, 그 나머지들은 소수일 것이다.
import math
prime_test = [False, False] + [True] * (N-1)
prime_list = []
m = int(math.sqrt(N))

for i in range(2, m+1):
    if prime_test[i]:
        for j in range(i*2, N+1, i):
            prime_test[j] = False

for i in range(len(prime_test)):
    if prime_test[i]:
        prime_list.append(i)

print("소수의 갯수", sum(prime_test), len(prime_list), sep=" : ")
print("소수들 = ", prime_list)