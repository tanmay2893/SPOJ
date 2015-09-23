
def merge(l,r,a):
    #print l
    #print r
    global count 
    nl,nr=len(l),len(r)
    #print nl
    #print nr
    
    i,j,k=0,0,0
    while i<nl and j<nr:
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            #print 'yay'
            count+=nl-i
            #print count
            a[k]=r[j]
            j+=1
        k+=1
    while i<nl:
        a[k]=l[i]
        i+=1
        k+=1
    while j<nr:
        a[k]=r[j]
        j+=1
        k+=1
    return a


def merge_sort(a):
    n=len(a)
    if n<2:
        return a
    mid=n/2
    left=a[:mid]
    right=a[mid:]
    #print left
    #print right
    #print '*********'
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right,a)
import sys
input_Data=sys.stdin.read()
input_Data = input_Data.split('\n\n')
t=int(input_Data[0])
total=t
#print input_Data
while t:
    t-=1
    g=input_Data[total-t].split('\n')
    #print g
    try:
        g.remove('')
        x=g
    except:
        x=g
    #print x
    l=map(int,x)[1:]
    count=0
    merge_sort(l)
    print count

