'''
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가
여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
은 22입니다.
'''

N, K = map(int, input("N, K를 띄어써서 입력하시오 : ").split())
data = list(map(int, input("N개의 숫자를 띄어써서 입력하시오 : ").split()))
# res = set() 이란 자료구조는 리스트와 비슷하게 작동하지만, 중복된 원소들을 한번만 취급해준다.
# list 에서 원소 추가는 append이지만, set에서는 add를 사용한다.
# 그런데, 이 set의 자료구조에는 sort기능이 없다. 따라서 sort하려면 list화를 다시 시켜줘야 한다.

res = set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(data[i]+data[j]+data[k]) # 중복된 결과는 다시 추가되지 않는다.

res = list(res) # sort하기 위한 set->list로 자료구조 변환
res.sort(reverse=True)
print(res[K-1])

