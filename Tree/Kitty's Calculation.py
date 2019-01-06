class root:
    def __init__(self,key, parent,depth):
        self.key = key
        self.parent = parent
        self.depth = depth
        
def cr_node(ch,parent):
    temp = root(ch,parent,parent.depth + 1)
    return temp
    
def crunch(u,v,N_key,Nodes):
    p_u = []; p_v = []; i = u; j = v
    u = N_key.index(u); u = Nodes[u]
    v = N_key.index(v); v = Nodes[v]
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
    return (i*j*dist)%((10**9) + 7)
        

nq = list(map(int, input().split()))
n = nq[0]; q = nq[1]
Nodes = []; N_key = []
for ite in range(n-1):
    pch = list(map(int, input().split()))
    p = pch[0]; ch = pch[1]
    if ch in N_key:
        i = N_key.index(ch)
        ch = Nodes[i]
        temp = root(p,None,ch.depth - 1)
        Nodes.append(temp)
        N_key.append(temp.key)
        ch.parent = temp
        
    elif p in N_key:
        i = N_key.index(p)
        p = Nodes[i]
        temp = cr_node(ch,p)
        Nodes.append(temp); 
        N_key.append(temp.key)
        
    else:
        temp = root(p,None,1)
        Nodes.append(temp)
        N_key.append(temp.key)
        
        temp2 = cr_node(ch,temp)
        Nodes.append(temp2); 
        N_key.append(temp2.key)

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
                ans.append(crunch(u,v,N_key,Nodes))
                n += 1
            m += 1; n = m + 1
        print(sum(ans))
        wait = True