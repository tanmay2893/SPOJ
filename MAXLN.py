t=int(raw_input(''))
total = t
while t:
    t-=1
    x=int(raw_input(''))
    ans=(4*x*x)+0.25
    print 'Case '+str(total-t)+': %.2f' %(ans)
    
