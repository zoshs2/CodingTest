import sys

def MaximumTip(tip_list):
    tip_list = sorted(tip_list, reverse=True) # Key-point
    maxtip = 0
    for i, tip in enumerate(tip_list):
        newtip = (tip - i)
        if newtip > 0:
            maxtip += newtip

    return maxtip

if __name__ == '__main__':
    n = int(input())
    tips = []
    for _ in range(n):
        tips.append(int(sys.stdin.readline()))

    answer = MaximumTip(tips)
    print(answer)