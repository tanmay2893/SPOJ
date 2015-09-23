def ans(n):
    return ((2*(n**3))+(3*(n**2))+n)//6
n=int(raw_input(''))
while n!=0:
    print ans(n)
    n=int(raw_input(''))
