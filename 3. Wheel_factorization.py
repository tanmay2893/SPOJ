def remove_multiples(x,l,b):
    for i in x:
        while i<=n:
            t=l.index(i)
            b[t]=False
            i+=i
    return [l],[b]

primes=[2,3]
n=6
l=[]
b=[]
l+=[[k for k in range(1,n+1)]]
b+=[[True for k in range(1,n+1)]]
print l
l,b=remove_multiples([2,3],l[0],b[0])
x=1
for i in range(1,4):
    l+=[[k for k in range((x*n)+1,((x+1)*n)+1)]]
    b+=[[True for k in range(n)]]
    print l
    print b
    x+=1
        
    
            

