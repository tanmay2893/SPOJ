
a,d=map(int,raw_input('').split(' '))
while a!=0 and d!=0:
    attackers=map(int,raw_input('').split(' '))
    defenders=map(int,raw_input('').split(' '))
    #print attackers
    attack=min(attackers)
    #print attack
    defenders.sort()
    #print defenders
    defend=defenders[1]
    #print defend
    if attack>=defend:
        print 'N'
    else:
        print 'Y'
    a,d=map(int,raw_input('').split(' '))
    
