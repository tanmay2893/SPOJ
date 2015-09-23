'''
def ans(s):
    #print s
    #raw_input('')
    if len(s)==1:
        #print (1,1,0)
        return (1,1,0)
    y=s[1:]
    #print y
    try:
        g=int(s[:2])
    except:
        g=0
    if g<=26:
        x=1
        #print x
    else:
        x=0
    a=ans(y)
    if x:
        b=2*a[0]-a[2]
        d=a[1]
        s=b-d
        #print (b,s,d)
        return (b,s,d)
    b=a[0]
    d=0
    s=b
    #print (b,s,d)
    return (b,s,d)
'''
s=raw_input('')
while s!='0':
    dp=[]
    l=len(s)
    for i in range(l):
        if i==0:
            dp+=[1]
        else:
            g=s[i-1:i+1]
            x=s[i]
            if x!='0' and int(g)<=9:
                dp+=[dp[i-1]]
            elif x!='0' and g<='26':
                dp+=[dp[i-1]+dp[i-2]]
            elif x=='0':
                dp+=[dp[i-2]]
            else:
                dp+=[dp[i-1]]
    print dp[-1]
    s=raw_input('')
