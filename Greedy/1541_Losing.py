# +, - 으로 이루어진 연산에다가 적절하게 ()를 설정하여 최소값을 산출하는 프로그램
# - 부호를 기준으로 나누고, 나눠진 요소들끼리 모두 합을 해서 new_NumList에 담는다.
# 예를 들어, new_NumList = [x,y,z,a,b,c] 로 담겼다고 하면
# 이것은 x - y - z - a - b - c라는 결과이다.
# 따라서 마지막으로 계산을 위해, new_NumList[0] - sum(new_NumList[1:]) 로 결과를 뽑아냄.
import sys

def CalculateMin(eq):
    new_NumList = []
    for term in eq:
        vals = term.split('+')
        temp = 0
        for val in vals:
            temp += int(val)
        
        new_NumList.append(temp)
        
    result = new_NumList[0] - sum(new_NumList[1:])
    return result

if __name__ == '__main__':
    equation = list(sys.stdin.readline().strip().split('-'))
    answer = CalculateMin(equation)
    print(answer)