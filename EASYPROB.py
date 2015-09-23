from math import *
numbers=[137,1315,73,136,255,1384,16385]
for n in numbers:
    g=n
    l=[n]
    ans=str(n)
    n=l.pop()
    dic={}
    while True:
        if n in dic:
            try:
                n=l.pop()
            except:
                break
            continue
        x=int(log(n,2))
        got=2**x
        rem=n-got
        if rem!=0:
            if x!=1:
                ans='2('+str(x)+')+'+str(rem)
            else:
                ans='2+'+str(rem)
        else:
            if x!=1:
                ans='2('+str(x)+')'
            else:
                ans='2'
        dic[n]=ans
        if x!=0 and rem!=0:
            l+=[x,rem]
        #print ans
        try:
            n=l.pop()
        except:
            break
    a=[]
    for i in dic:
        a+=[i]
    a.sort()
    ans=str(g)
    while True:
        try:
            x=a.pop()
        except:
            break
        ans=ans.replace(str(x),dic[x])
    final=str(g)+'='+ans
    print final
        
