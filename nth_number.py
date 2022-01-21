'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''

T = int(input("몇 개의 케이스인가요? : "))

for _ in range(T):
    N, s, e, k = map(int, input("N, s, e, k를 띄어써서 입력하세요 : ").split())
    # 이제 N개의 데이터를 입력받을 차례
    data = list(map(int, input("N개의 숫자 데이터들을 씌어써서 입력하세요 : ").split()))
    data = data[s-1:e]
    data.sort()
    print(data)
    print(data[k-1])



