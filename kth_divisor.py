'''
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
작성하시오.
'''
n, k = map(int, input("두 개의 자연수 입력(띄어쓰기로 구분) : ").split())
# print(type(a), type(b), sep=" & ")
# print("a :", a, "b :", b, sep=" ")

def kth_divisor(n,k):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1
        
        if cnt == k:
            print("We find the k-th divisor of N")
            return i
        
    else: # for-else 문이다. for 문이 중간에 break 등으로 끊키지 않고, 끝까지 수행되었을 때 작동하는 구문이다. if-else문만 알고 있다면, for-else도 알아두자!
        print(-1)
        print(12)
        return -1

result = kth_divisor(n,k)
print("result : ", result)

