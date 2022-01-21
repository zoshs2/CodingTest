N = int(input())
if (N%5)%3!=0 and (N%3)%5!=0:
    print("-1")

else:
    if (N%5)%3!=0:
        print(N//3)
    else:
        print((N//5)+(N%5)//3)
