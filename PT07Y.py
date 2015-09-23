from test import submit
nodes,edges=map(int,raw_input('').split(' '))
def evaluate_fringe(x):
    global done,fringe,visited
    if visited[x]:
        return False
    done+=[x]
    visited[x]=True
    #print x
    #print done
    try:
        t=edge_dict[x]
        fringe+=t
        #print t
        for i in t:
            edge_dict[i].remove(x)
            #print '*********'
            #print edge_dict
    except:
        pass
    #print fringe
    #raw_input('')
    return True
list_of_edges=[]
if edges+1!=nodes:
    ans='NO'
    while edges:
        edges-=1
        raw_input('')
    print ans
else:
    edge_dict={}
    while edges:
        edges-=1
        x,y=map(int,raw_input('').split(' '))
        list_of_edges+=[x,y]
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
    g=len(list(set(list_of_edges)))
    if g<nodes:
        print 'NO'
    else:
        done=[]
        visited=[False]*(nodes+1)
        fringe=[1]
        ans='not done'
        while True:
            try:
                i=fringe.pop()
                g=evaluate_fringe(i)
                if g==False:
                    ans='done'
                    print 'NO'
                    break
            except:
                break
        if ans!='done':
            if len(done)==nodes:
                print 'YES'
            else:
                print 'NO'

