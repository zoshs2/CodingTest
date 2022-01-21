i = 0
loop_info = []
num = int(input("루프 갯수:")) 
while i < num:
    data = int(input("루프 허용중량:"))
    loop_info.append(data)
    i += 1

loop_info = sorted(loop_info)
answer = loop_info[-1] # Assumed answer

for i, min_loop in enumerate(loop_info):
    total_loop = min_loop * (num - i)
    if total_loop <= answer:
        continue

    else:
        answer = total_loop

else:
    if answer > 10000:
        answer = 10000

print(answer)

'''
통과된 코드
* 정답 이외에 출력되는 문자는 없어야 함. 있으면 '출력초과'라는 에러가 뜸.
* for loop (또는 while loop) 반복문을 통해, 입력을 받을 때 input() 을 사용하면 
    '시간초과' 에러가 발생할 수 있다. 대표적인 예시가 백준의 BOJ 15552번 문제.
    따라서 코테에서는 여러줄 입력을 받아야할 때, sys.stdin.readline() 을 주로 사용한다고 한다.

i = 0
loop_info = []
num = int(input())
while i < num:
    data = int(input())
    loop_info.append(data)
    i += 1

loop_info = sorted(loop_info)
answer = loop_info[-1] # Assumed answer

for i, min_loop in enumerate(loop_info):
    total_loop = min_loop * (num - i)
    if total_loop <= answer:
        continue

    else:
        answer = total_loop
        
print(answer)
'''