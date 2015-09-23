def to_matrix(l, n):
    return [l[i:i+n] for i in xrange(0, len(l), n)]

def ans(c,s):
    length=len(s)
    rows=length/c
    x=to_matrix(s,c)
    for i in range(len(x)):
        if i%2==0:
            x[i]=list(x[i])
        else:
            a=list(x[i])
            a.reverse()
            x[i]=a
    ans=''
    for j in range(c):
        for i in range(rows):
            ans+=x[i][j]
    print ans

c=int(raw_input(''))
while c!=0:
    s=raw_input('')
    ans(c,s)
    c=int(raw_input(''))
        
