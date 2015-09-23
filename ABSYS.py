def ans(s):
    x=s.split('=')
    answer=x[1]
    find_answer,find_op1,find_op2=0,0,0
    left=x[0]
    x=left.split('+')
    op1=x[0]
    op2=x[1]
    try:
        answer=int(answer)
        try:
            op1=int(op1)
            find_op2=1
        except:
            find_op1=1
            op2=int(op2)
    except:
        find_answer=1
        op1=int(op1)
        op2=int(op2)
    if find_answer:
        ans=op1+op2
        return str(op1)+' + '+str(op2)+' = '+str(ans)
    elif find_op1:
        ans=answer-op2
        return str(ans)+' + '+str(op2)+' = '+str(answer)
    else:
        ans=answer-op1
        return str(op1)+' + '+str(ans)+' = '+str(answer)
    
t=int(raw_input(''))
while t:
    t-=1
    raw_input('')
    s=raw_input('')
    print ans(s)
