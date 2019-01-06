class root:
    def __init__(self,key, parent,depth):
        self.key = key
        self.parent = parent
        self.depth = depth
        
def cr_node(ch,parent):
    temp = root(ch,parent,parent.depth + 1)
    return temp
    
def crunch(u,v,index):
    p_u = []; p_v = []; i = u; j = v
    u = index[u]; v = index[v];
    while u.depth != v.depth:
        if v.depth > u.depth:
            p_v.append(v.parent.key)
            v = v.parent
        else:
            p_u.append(u.parent.key)
            u = u.parent
    while u.parent and v.parent:
        if u.parent.key == v.parent.key:
            p_v.append(v.parent.key)
            p_u.append(u.parent.key)
            break
        else:
            p_v.append(v.parent.key)
            p_u.append(u.parent.key)
            u = u.parent; v = v.parent
    dist = len(p_v) + len(p_u)
    return (i*j*dist)
        
import time
x = time.clock()
nq = list(map(int, input().split()))
n = nq[0]; q = nq[1]
Nodes = []; N_key = []; index = []
for i in range(n+1):
    index.append(None)
for ite in range(n-1):
    pch = list(map(int, input().split()))
    p = pch[0]; ch = pch[1]
    if not index[p] and not index[ch]:
        temp = root(p,None,1); temp2 = cr_node(ch,temp)
        index[p] = temp; index[ch] = temp2
        
    elif index[p] and not index[ch]:
        temp = index[p];  temp2 = cr_node(ch,temp)
        index[ch] = temp2
        
    elif not index[p] and index[ch]:
        temp = index[ch];  temp2 = cr_node(p,temp)
        index[p] = temp2

wait = True
for ite in range(2*q):
    if wait:
        k = int(input())
        wait = False
            
    else:
        ks = list(map(int, input().split()))
        m = 0; n = 1; ans = []
        while m != len(ks):
            u = ks[m]
            while n != len(ks):
                v = ks[n]
                ans.append(crunch(u,v,index))
                n += 1
            m += 1; n = m + 1
        print(sum(ans)%(10**9 + 7))
        wait = True
print('running time =', (time.clock()-x))
