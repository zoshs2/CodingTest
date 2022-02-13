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
        for i in range(len(obj)):
            test = obj[:]
            test.pop(i)
            if ''.join(test[::-1]) == ''.join(test):
                answer.append(str(1))
                break
        else:
            answer.append(str(2))            

print('\n'.join(answer))