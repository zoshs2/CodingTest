'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게
임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된
다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금
으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
을 작성하시오

입력예제
3 
3 3 6
2 2 2
6 2 5

출력예제
12000
'''

'''
N = int(input("몇 명이서 게임하는 지 입력하시오 : "))

data = [] 
for i in range(N):
    data.append(list(map(int, input("{}번째 친구의 데이터를 띄어써서 입력하시오 : ".format(i+1)).split()))) # 2차원 리스트

''' # 300명 이러면 900개 데이터를 일일히 써야되서 이건 못참겠다. 파일을 불러오자.
import os

for dirname, _, filenames in os.walk("/Users/yungi/Documents/대학원졸업/코딩테스트/inf_learn/pythonalgorithm_formac/section_2/dice_game"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

dataset = []
with open('/Users/yungi/Documents/대학원졸업/코딩테스트/inf_learn/pythonalgorithm_formac/section_2/dice_game/in5.txt', 'rt') as datafile:
    N = datafile.readline() # 한 줄만 읽는겨
    print("게임하는 플레이어 수는 {}명 입니다.".format(N))
    for line in datafile.readlines(): # readlines() 는 한 줄씩 리스트에 담겨서 따로따로 저장된다. 
        # line은 '3 2 1 \n' 와 같은 string 이다.
        data = line.rstrip('\n').split() # 한줄씩 떼어왔기 때문에, 오른쪽 끄트머리 부분에 \n 이 달려있다. 그래서 rstrip()함수로 \n를 제거한다. 
        # 제거 후 나머지 숫자들은 띄어쓰기로 구분되어 있기 때문에, .split()함수를 써서, 각기 다른 element들이라 가르쳐준다. --> 총 결과는 하나의 리스트 형태로 반환된다.
        # 애초에 string 객체 자체가 iterable 하고 list처럼 동작하는데, 하나의 리스트 처럼 동작하는 string 을 split 하면, 따로따로 나뉘어 list에 담겨 반환되는 것이다.
        tmp = list(map(int, data))
        if not tmp: # tmp = [] 이처럼 비어있는데, 그런 리스트에 "not이니?(비어있니?)" 라고 물어보면 "응(True)"라고 대답한다.
            break
        dataset.append(tmp)
        
# print(dataset)

result = []
def reward(x):
    high_num = max(x)
    x_set = set(x)
    if len(x_set) == 3:
        return high_num*100

    elif len(x_set) == 2:
        for num in x_set:
            if x.count(num) == 2:
                return 1000+(num)*100
            else:
                continue

    else: # len(x_set) == 1인 경우(모두가 같은 경우)겠죠?
        return 10000+(x[0])*1000


for x in dataset:
    result.append(reward(x))

print(max(result))
