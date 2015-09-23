'''
def ans(n):
    x=int(n)
    if x<10:
        return n
    l=len(n)
    if n=='9'*l:
        return '1'+('0'*(l-1))+'1'
    if l%2==0:
        a=n[:l/2]
        b=n[l/2:]
        c=''
        if a==b[::-1]:
            x=str(int(a)+1)
            return (x+x[::-1])
        else:
            x,y=int(a),int(b)
            if int(a[::-1])>y:
                return a+a[::-1]
            else:
                n=str(x+1)
                return n+n[::-1]
    else:
        a=n[:l//2]
        b=n[l//2+1:]
        c=n[l//2]
        if a==b[::-1]:
            x=str(int(a+c)+1)
            #print x
            y=x[:-1]
            #print y
            return y+x[-1]+y[::-1]
        else:
            x,y=int(a),int(b)
            if int(a[::-1])>y:
                return a+c+a[::-1]
            else:
                x=str(int(a+c)+1)
                y=x[:-1]
                return y+x[-1]+y[::-1]
'''
def inc(left):
    leftlist=list(left) 
    last = len(left)-1 
    while leftlist[last]=='9': 
        leftlist[last]='0'
        last-=1
    
    leftlist[last] = str(int(leftlist[last])+1)
    return "".join(leftlist)
def ans(n):
    size=len(n)
    odd=size%2
    mid=size/2
    if int(n)<10:
        return n
    if n=='9'*size:
        return '1'+(size-1)*'0'+'1'
    if odd:
        center=n[mid]
    else:
        center=''
    left=n[:mid]
    right=left[::-1]
    pdrome=left+center+right
    if pdrome>n:
        return pdrome
    if center:
        if center<'9':
            center=str(int(center)+1)
            return left+center+right
        else:
            center='0'
    left=inc(left)
    return left+center+left[::-1]
t=int(raw_input(''))
while t:
    t-=1
    s=raw_input('')
    print ans(s)

'''
for i in range(10000000):
    print ans(str(i))
'''
