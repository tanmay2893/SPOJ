memo={0:0}
def ans(n):
    if n in memo:
        return memo[n]
    if n%12!=0:
        memo[n]=n
        return n
    else:
        r=max(((13*n)/12),(ans(n//2)+ans(n//3)+ans(n//4)))
        memo[n]=r
        return r   
print ans(12000)
