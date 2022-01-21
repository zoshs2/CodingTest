# 최소값 구하기 알고리즘
arr = [5,3,2,8,9,12,15,1,63,7]
arrMin = float('inf') # 파이썬에서 지정할 수 있는 '가장 큰 값!' infinity : 무한대
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]  # 사실상 이걸로 끝난다. 
print(arrMin)

# 또는 arrMin을 inf로 초기화하는 게 마음에 들지 않는다면, 그냥 해당 대상 array의 첫 번째 원소를 arrMin로 임의초기화해도 알고리즘 과정은 여전히 유효하다. 
arrMin = arr[0]
for i in range(1, len(arr)): 
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)


