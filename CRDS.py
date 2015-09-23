t=int(raw_input(''))
while t:
    t-=1
    x=int(raw_input(''))
    ans=(3*(x*x)+x)//2
    print ans%1000007
