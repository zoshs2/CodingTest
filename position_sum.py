'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.

** 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자를 출력합니다.
'''

N = int(input("몇 개(N)의 자연수를 입력할 것인지 입력하시오 : "))
data = list(map(int, input("N개의 자연수를 띄어써서 입력하시오 : ").split()))
    
def digit_sum(x):
    num = [] # 자리마다 수를 넣을 리스트
    x = str(x) # 숫자를 string 으로 전환 (-> 배열로 활용가능)
                # length = len(x) # 몇 자리 숫자인지 계산
    for i in range(len(x)):
        num.append(int(x[i]))


    return sum(num)

high_sum = -1
high_sum_num = 0

for i in range(N):
    res = digit_sum(data[i])
    if res == high_sum:
        continue  # 같다면 건너띄고 계속해

    elif res > high_sum:
        high_sum = res
        high_sum_num = data[i]

print(high_sum_num)