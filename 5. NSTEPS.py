def ans(x,y):
    mod=x%2
    if x==y:
        if mod==0:
            return 2*x
        else:
            return ((x//2)*4)+1
    elif y==x-2:
        if mod==0:
            return 2+(((x/2)-1)*4)
        else:
            return 3+(((x//2)-1)*4)
    else:
        return 'No Number'
n=int(raw_input(''))
while n:
    n-=1
    x,y=map(int,raw_input('').split(' '))
    print ans(x,y)
