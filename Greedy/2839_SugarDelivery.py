def solution(kilo):
    # 3의 최대 몫을 기준으로, 몫 0부터~ loop를 돌리면서,
    # if 조건문이 성립되는 순간이 최소 봉지 갯수이다.
    # 성립되는 조건이 없다면, 어떤 방식으로든 딱 떨어지게 담을 수 없는 경우이므로
    # for문을 벗어나면 -1을 반환한다.
    for quo in range((kilo//3)+1): 
        if (kilo - 3*quo) % 5 == 0: 
            return ((kilo - 3*quo) // 5) + quo
    return -1
        
if __name__ == '__main__':
    N = int(input())
    print(solution(N))