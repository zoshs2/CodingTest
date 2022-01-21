'''
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다.

입력예제
5
32 55 62 3700 250

출력예제
23 73
'''

N = int(input("자연수 갯수를 입력하세요 : "))
data = list(input("N개의 자연수를 띄어써서 입력하세요 : ").split()) # 처음부터 그냥 string 으로 받아

# slicing a[시작위치:끝나는위치:stepsize] e.g. a[::2] 이러면, 그냥 처음부터 끝까지 (default라 생략) 2개 스텝사이즈로 추출하라는 거
def reverse(x):
    y = x[len(x)::-1]
    return int(y)

def isPrime(x):
    if x == 1:
        return False

    for div in range(2, x):
        if x%div == 0:
            return False
    else:
        return True

tmp = []
for idx, x in enumerate(data):
    data[idx] = reverse(x)

for y in data:
    if isPrime(y):
        tmp.append(y)

print(tmp)


