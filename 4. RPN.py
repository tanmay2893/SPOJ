def RPN(s):
    stack=[]
    output=''
    for i in s:
        if i=='(':
            continue
        if i==')':
            a=stack.pop()
            #print a
            output+=a
            #print stack
            continue
        if ord(i)<97:
            stack.append(i)
        else:
            output+=i        
    print output


n=int(raw_input(''))
while n:
    n-=1
    s=raw_input('')
    RPN(s)
    
