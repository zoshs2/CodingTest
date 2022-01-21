N, M = map(int, input("정 N면체와 정 M면체를 띄어써서 정하시오 : ").split())

N_res = [x+1 for x in range(N)]
M_res = [y+1 for y in range(M)]
sum_list = []
sum_set = set()
for i in range(len(N_res)):
    for j in range(len(M_res)):
        sum_list.append(N_res[i]+M_res[j])
        sum_set.add(N_res[i]+M_res[j])

#print(sum_list)
#print(sum_set)

res = dict()
for x in sum_set:
    cnt = sum_list.count(x)
    res[x] = cnt

res = sorted(res.items(), key=(lambda x: x[1]), reverse=True) # value기준으로 dictionary 정렬하기 -> list속 tuple이 있는 형태로 반환
val_tmp = 0
high_num = []

for key, val in res:
    if val >= val_tmp: 
        high_num.append(key)
        val_tmp = val
    
    else:
        break

print(high_num)