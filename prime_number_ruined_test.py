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

num_list = []
for i in range(2, N+1):
    num_list.append(i)

no_prime = []
cnt = 0
# 즉, 나는 no_prime을 먼저 담고 나중에 전체에서 걸러낼거여.
# 근디 이렇게하면, ... 다 돌죠. 20만 넣으면, 20만^2 복잡성을 가진다. 슈방.. 개망..
for i in range(len(num_list)):
    # prime_list.append(num_list[i])
    for j in range(i+1, len(num_list)):
        if num_list[j]%num_list[i] == 0:
            no_prime.append(num_list[j])          

# num_list에서 no_prime 리스트를 빼주면, 남는 숫자들이 소수겠지. => 에라토스테네스 체
# 근데 이 짓거리를 하려면, 리스트끼리 연산은 안되기 때문에, set을 이용한다!
# set은 set끼리 연산이 가능 ~!!
num_set = set(num_list)
no_prime_set = set(no_prime)

prime_list = list(num_set-no_prime_set)
print(len(prime_list))