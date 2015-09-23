def ans(n):
    d=int(-1 + (1 + 8*n)**0.5)/2
    e=int(n-d*(d+1)/2)
    if e<= 1:
        v1,v2 = d + e,1
    else:
        v1,v2 = d-e+2,e
    if d % 2 == 0:
        answer = str(v1) + '/'+ str(v2)
    else:
        answer = str(v2) + '/'+ str(v1)
    return answer
t=int(raw_input(''))
while t:
    t-=1
    n=int(raw_input(''))
    print "TERM " + str(n) + " IS " + ans(n)
