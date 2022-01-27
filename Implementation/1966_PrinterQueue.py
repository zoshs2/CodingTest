from collections import deque

def solution():
    return

if __name__ == '__main__':
    NumCase = int(input())
    Answers = []
    for _ in range(NumCase):
        NumSample, Target = map(int, input().split())
        if NumSample == 1:
            Answers.append(1)
        else:
            Answers.append(solution())
