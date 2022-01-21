msg = "It is Time"
print(msg.upper())
tmp = msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # alphabet (알파벳) 일때만 True!
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x)) # ord(x) : x를 ASCII number로 출력해준다.
print()

tmp = 'az'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp)) # tmp 에 해당하는 ASCII 문자로 변환해준다. chr(x)

a = list(range(1,11))
print(a)

import random as r
r.shuffle(a)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.clear()
print(a)
