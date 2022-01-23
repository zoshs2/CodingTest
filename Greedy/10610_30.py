# 자연수의 배수 판정법에 대해 알면 쉽게 풀 수 있다.
# 이 문제는 30배수가 되는 최대 숫자를 조합해서 찾는 문제이다.
# 2의 배수는 끝자리인 일의 자리가 0,2,4,6,8 인지만 확인하면 끝나듯이 말이다.
# 3의 배수는 모든 자릿 수의 합이 3의 배수면, 3의 배수이다.
# 10의 배수는 일의 자리가 0이면, 10의 배수이다.
# 30 배수는 10의 배수 및 3의 배수 판정법을 활용해서,
# "일의 자리가 0이면서 동시에 자릿수 합이 3의 배수"면 된다.
import sys

if __name__ == '__main__':
    data = list(sys.stdin.readline().strip())
    if '0' not in data:
        print(-1)
    else:
        indicator = 0
        answer = ''
        data = sorted(data, reverse=True)
        for val in data:
            answer += val
            indicator += int(val)
        
        if indicator % 3 != 0:
            print(-1)
        else:
            print(int(answer))