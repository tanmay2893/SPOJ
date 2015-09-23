t=int(raw_input(''))
while t:
    t-=1
    n,p=map(int,raw_input('').split(' '))
    if p==0:
        print 'Airborne wins.'
    else:
        print 'Pagfloyd wins.'
