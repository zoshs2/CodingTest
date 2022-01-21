n = int(input()) # 그냥 input으로 받으면 string 으로 받는다. 그래서 숫자를 받을거면 int나 flot으로 묶어준다.
for i in range(1, n+1):
    if i%2==1: # 홀수
        print(i)
