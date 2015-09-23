
x=int(raw_input(''))
while x!=-1:
    if x==1:
        print 'Y'
    else:
        x-=1
        a=((48*x)+36)**0.5
        if a==int(a):
            print 'Y'
        else:
            print 'N'
    x=int(raw_input(''))
