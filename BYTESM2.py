t=int(raw_input(''))
while t:
    t-=1
    r,c=map(int,raw_input('').split(' '))
    x=[[0 for i in range(c)] for j in range(r)]
    ans=x[:]
    for i in range(r):
        x[i]=map(int,raw_input('').split(' '))
    #print x
    ans[0]=x[0]
    #print ans

    for i in range(1, r):
        for j in range(c):
            if j!=0 and j!=c-1:
                ans[i][j]=x[i][j]+max(ans[i-1][j],ans[i-1][j-1],ans[i-1][j+1])
            elif j==0:
                ans[i][j]=x[i][j]+max(ans[i-1][j],ans[i-1][j+1])
            else:
                ans[i][j]=x[i][j]+max(ans[i-1][j],ans[i-1][j-1])
    #print ans
    print max(ans[-1])

