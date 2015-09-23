from test import submit
s="""
def ans(l):
    answer=int(l[0])
    op='nothing'
    for i in l[1:]:
        try:
            i=int(i)
            if op=='+':
                answer+=i
            elif op=='*':
                answer*=i
            elif op=='/':
                answer/=i
            else:
                answer-=i
        except:
            op=i
    return answer

               
test=int(raw_input(''))
import re
while test:
    test-=1
    raw_input('')
    s=raw_input('')
    s=s[:-1]
    s=s.replace(' ','')
    s=re.split('(["+","*","/","-"])',s)
    print ans(s)"""
submit(s,'ARITH2')
