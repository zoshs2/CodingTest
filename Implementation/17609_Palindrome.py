import sys
N = int(input())
answer = []
for _ in range(N):
    obj = list(sys.stdin.readline().strip())
    if len(obj)%2==0:
        front = obj[:len(obj)//2]
        back = obj[len(obj)//2:]
        for f, b in zip(front[::-1], back):
            if f != b:
                answer.append(str(2))
                break
            else:
                continue
        else:
            answer.append(str(0))

    else:
        back = obj[::-1]
        iternum = len(obj)
        for _ in range(iternum//2):
            back.pop(0) 
            obj.pop(0)
            if ''.join(back) == ''.join(obj):
                answer.append(str(1))
                break
        else:
            answer.append(str(2))
            

            
print('\n'.join(answer)) # 답