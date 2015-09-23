def ans(pg,pm):
    max_pg=max(pg)
    max_pm=max(pm)
    if max_pg>=max_pm:
        print 'Godzilla'
    else:
        print 'MechaGodzilla'
    '''
    while len(pg)!=0 and len(pm)!=0:
        if pg[0]<pm[0]:
            pg.pop(0)
        else:
            pm.pop(0)
    if len(pm)==0:
        print 'Godzilla'
    else:
        print 'MechaGodzilla'
    '''
t=int(raw_input(''))
while t:
    t-=1
    raw_input('')
    ng,nm=map(int,raw_input('').split(' '))
    if ng==1:
        pg=[int(raw_input(''))]
    else:
        pg=map(int,raw_input('').split(' '))
    if nm==1:
        pm=[int(raw_input(''))]
    else:
        pm=map(int,raw_input('').split(' '))
    ans(pg,pm)
	
