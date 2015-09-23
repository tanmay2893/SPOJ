n=int(raw_input(''))
while n:
    n-=1
    x=raw_input('')
    students=int(raw_input(''))
    c=students
    total=0
    while c:
        c-=1
        total+=int(raw_input(''))
    if total%students==0:
        print 'YES'
    else:
        print 'NO'
        
