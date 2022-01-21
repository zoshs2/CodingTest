# 파이썬의 round 반올림 및 반내림 함수.
# 가장 '가까운 배수'로 반올림 및 반내림한다. 
# 우리가 일반적으로 알고 있는, '몇 번짜리에서 5이상일 때 올린다' 라는 반올림 로직하고는 약간 다르게 작동한다!!
# 이 차이는 반올림을 하고자 하는 자릿수의 숫자가 5일때 발생하는데,
# 예컨대, 0.5, 2.5, 4.5, ... 와 같은 수를 소수점 아래 첫 째자리에서 반올림한다면,
# 우리는 1, 3, 5, ... 라고 생각될텐데. 
# 파이썬의 round 함수는 그렇지 않다. 
# round 함수는 이럴 경우 0, 2, 4 로 반'내림'을 수행한다.. 
# 이는 반올림하고자 하는 자릿수가 절반(5)으로 걸쳐있을 때는, 
# 바로 "" 앞 자릿수가 홀수면 올리고, 짝수면 내리는 방식 "" 을 취하는 것이다.
# 이런 방식을 Bankers' rounding 또는 Gaussian rounding 또는 round half to even 이라고 한다더라.. 
# (** Python v2.7 이하에서는 우리가 흔히 알고있는 반올림 방식대로 작동한다. 그런데 Python v3.x 이상부터는 이게 바뀐 것)

# The simple "always round 0.5 up" technique results in a slight bias toward the higher number. 
# With large numbers of calculations, this can be significant. The Python 3.0 approach eliminates this issue.

'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

입력 예제 
10 
45 73 66 87 92 67 75 79 75 80

출력(답)
74 7
'''


N = int(input("학생이 몇 명(N)인지 입력하시오 : "))
math_res = list(map(int, input("N명의 수학 점수를 띄어써서 입력하시오 : ").split()))
math_avg = int(round(sum(math_res)/len(math_res), 0)) # 첫째 자리에서 반올림하면 어차피 정수니가 int로 형변환!
diff_num = float('inf')

for i in range(1, len(math_res)):
    diff_tmp = abs(math_avg - math_res[i])
    if diff_tmp < diff_num:
        diff_num = diff_tmp
        close_num = math_res[i]
    
    elif diff_tmp == diff_num and math_res[i] > close_num:
        close_num = math_res[i]

'''
high_id = -1
for i in range(len(math_res)):
    if math_res[i] == close_num and i > high_id:
        high_id = i 
아 이건 학생번호가 젤 나중인 경우이다. 
가장 빠른 경우를 뽑으려면 그냥 list의 index() 메소드를 쓰면 된다.

'''
print(close_num)
print("math_avg = {}, close_id = {}".format(math_avg, math_res.index(close_num)+1))
# 컴퓨터에서 말하는 순서 index는 일상문제의 순서보다 1이 낮다 ㅡ ㅡ 0부터 시작하니까. 
# 그러니까 일상문제 언어로 바꾸려면 1을 더해줘야 한다(+1). 이 바보 멍텅아