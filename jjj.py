'''N,K = map(int, input("N, K를 enter로 입력하세요").split(","))
print("N :", N, " K : ", K)
'''
data=list(map(int, input("데이터 입력 : ").split()))
print("for문 돌리기 전 data : " , data)

L=len(data)

for i in range(L):
    print(i) 