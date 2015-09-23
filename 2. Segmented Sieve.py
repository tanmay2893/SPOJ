def seg_sieve(a,b):
    n=int((b**0.5)+1)
    init_sieve=sieve(n)
    A=range(a,b+1)
    for i in init_sieve:
        x=(a//i)*i
        j=0
        while True:
            try:
                A.remove(x)
                x+=i
            except:
                if x<b:
                    j=1
                    x+=i
                    continue
                else:
                    break
    return A

def sieve(n):
    l=range(2,n+1)
    i=0
    p=l[i]
    while p<n**0.5:
        try:
            p=l[i]
            t=l[i]*l[i]
        except:
            break
        g=1
        x=t
        while x<n+1:
            try:
                l.remove(x)
                x=t+(g*p)
                g+=1
            except:
                g+=1
                x=g*p
                continue
        i+=1
    print l
    raw_input('')
    return l

print seg_sieve(10000,30000)
