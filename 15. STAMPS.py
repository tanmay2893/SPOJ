t=int(raw_input(''))
initial=t
while t:
    t-=1
    a,b=map(int,raw_input('').split(' '))
    x=map(int,raw_input('').split(' '))
    if sum(x)<a:
        print 'Scenario #'+str(initial-t)+':'
        print 'impossible\n'
        continue
    x.sort()
    x=x[::-1]
    total=0
    i=0
    while total<a:
        total+=x[i]
        i+=1
    print 'Scenario #'+str(initial-t)+':'
    print str(i)+'\n'
        
        
    
    
