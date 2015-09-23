def remove_multiples(x,l,b):
    base_index=[]
    other_index=[]
    for i in x:
        base_index+=[l.index(i)]
        j=i
        while j<=n:
            t=l.index(j)
            if j!=i:
                other_index+=[t]
                b[t]=False
            j+=i
    #print b
    return [l],[b],base_index,other_index

primes=[2,3]
n=6
l=[]
b=[]
l+=[[k for k in range(1,n+1)]]
b+=[[True for k in range(1,n+1)]]
#print l
l,b,base_index,other_index=remove_multiples([2,3],l[0],b[0])
#print b
b[0][0]=False
x=1
for i in range(1,10000):
    l+=[[k for k in range((x*n)+1,((x+1)*n)+1)]]
    b+=[[True for k in range(n)]]
    #print l
    #print b
    x+=1
        
for i in b[1:]:
    for j in base_index:
        i[j]=False
for i in b:
    for j in other_index:
        i[j]=False
#print b
l1=len(b)
l2=len(b[0])
final=[]
for i in range(l1):
    for j in range(l2):
        if b[i][j]==True:
            final+=[l[i][j]]
print final
            

