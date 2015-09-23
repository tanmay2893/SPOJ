import sys
lines=sys.stdin.readlines()
final_answer=''
for i in lines[1:]:
    x=i[:-1]
    a,b=map(int,x.split(' '))
    n=b
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
    index=0
    for k in range(len(l)):
        if l[k]>=a:
            index=k
            break
    l=l[k:]
    
    for i in l:
        final_answer+=str(i)+'\n'
    final_answer+='\n'
sys.stdout.write(final_answer)
