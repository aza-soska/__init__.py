def azamat(x):
    a=0
    for i in range(0,len(x)):
        if x[i]%2==0:
            print(x[i], end=" ")
        if x[i]%2!=0:
            a+=1
            if a==len(x):
                print(-1)


s=list(map(int,input().split()))
azamat(s)