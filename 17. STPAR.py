t=int(raw_input(''))
while t:
    a=map(int,raw_input('').split(' '))
    a=a[::-1]
    ans='yes'
    #print a
    i=1
    stack=[]
    while a!=[] or stack!=[]:
        #raw_input('')
        #print a
        try:
            k=a[-1]
        except:
            k=100000
        #print k
        #print a
        try:
            m=stack[-1]
            #print m
            if m==i:
                #print 'esadf'
                h=stack.pop()
            else:
                #print 'asdf'
                h=a.pop()
        except:
            #print 'asdfdsaf'
            h=a.pop()
            #print h
            #print a
        if h==i:
            #print h
            i+=1
        else:
            try:
                g=stack[-1]
                if g<h:
                    ans= 'no'
                    break
            except:
                pass
            stack.append(h)
            #print stack
    print ans
    t=int(raw_input(''))
