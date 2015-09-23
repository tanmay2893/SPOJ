def evaluate_fringe(x):
    global fringe
    t=edge_dict[x]
    fringe=t+fringe
    for i in t:
        edge_dict[i].remove(x)
    return len(t)
            
t=int(raw_input(''))
nodes=t
edge_dict={}
while (t-1):
    t-=1
    x,y=map(int,raw_input('').split(' '))
    try:
        l=edge_dict[x]
        edge_dict[x]=l+[y]
    except:
        edge_dict[x]=[y]
    try:
        l=edge_dict[y]
        edge_dict[y]=l+[x]
    except:
        edge_dict[y]=[x]
import copy
temp=copy.deepcopy(edge_dict)
fringe=[1]
last=1
while True:
    try:
        i=fringe.pop()
        last=i
        evaluate_fringe(i)
    except:
        break
fringe=[last]
length=0
edge_dict=copy.deepcopy(temp)
while True:
    try:
        print fringe
        i=fringe.pop()
        print i
        last=i
        g=evaluate_fringe(i)
        if g>1:
            length-=g
        length+=1
        print fringe
        print 'asdasdfasdsadadsf'
    except:
        break
print length-1
