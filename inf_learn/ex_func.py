'''
def add(a, b):
    c = a + b
    print(c)

add(3,2)
'''

def isPrime(x):
    for i in range(2,x): # 소수(prime)을 걸러내는 loop
        if x%i==0:
            return False

    return True


a = [1,2,3]
print(list(map(lambda x: x+1, a)))
