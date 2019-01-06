class root:
    def __init__(self,key,sig,anc,depth):
        self.key = key
        self.sig = sig
        self.anc = anc
        self.depth = depth
        
def cr_node(ch,parent):
    sig = parent.sig + str(parent.key);
    anc = parent.anc * 1; anc.append(parent.key);
    depth = parent.depth * 1; depth = parent.depth + [parent.depth[-1] + 1]*len(str(parent.key))
    tmp = root(ch,sig,anc,depth);
    return tmp;
    
def crunch(u,v,index):
    m = u; n = v; go = True; diff = 0
    u = index[u]; v = index[v]; 
    p = len(u.anc); q = len(v.anc)
    if len(v.anc) == 0 or len(u.anc) == 0 or u.anc[0] == v.anc[0]:
        if p > q:
            u,v = v,u; p,q = q,p
        i = q - p
        if i:
            if v.anc[len(v.anc)-i] == u.key:
                dist = i
                go = False
            else:
                diff = i; tmp = v.anc[len(v.anc)-i]
                v = index[tmp]
                 
        if go:
            i = len(v.sig); j = len(u.sig)
            if i > j:
               temp2 = u.sig + "0" * (i - j);
               waste = abs(int(v.sig) - int(temp2));
               if waste:
                   waste = len(str(waste))
               a = v.depth[len(v.depth) - waste - 1]; a -= 1
    
            else:
               temp2 = v.sig + "0" * (j - i); 
               waste = abs(int(u.sig) - int(temp2));
               if waste:
                   waste = len(str(waste))
               a = u.depth[len(u.depth) - waste - 1]; a -= 1
            while v.anc[a] != u.anc[a]:
                a -= 1
            dist =  (len(u.anc) - a) * 2 + diff
        return m*n*int(dist)

            
        
    
    #else:
        

##import time
##x = time.clock()
nq = list(map(int, input().split()))
n = nq[0]; q = nq[1]
index = [None]*(n+1);
for ite in range(n-1):
    pch = list(map(int, input().split()))
    p = pch[0]; ch = pch[1]
    if not index[p] and not index[ch]:
        tmp = root(p,'',[],[0]); temp2 = cr_node(ch,tmp) 
        index[p] = tmp; index[ch] = temp2

    elif index[p] and index[ch]:
        print("why")
        tmp = index[p]; temp2 = index[ch];
        temp2.sig = tmp.sig + str(tmp.key)
        temp2.anc = (tmp.anc)*1; temp2.anc.append(tmp.key)
   
    elif index[p] and not index[ch]:
        tmp = index[p];  temp2 = cr_node(ch,tmp)
        index[ch] = temp2
        
    elif not index[p] and index[ch]:
        tmp = index[ch];  temp2 = cr_node(p,tmp)
        index[p] = temp2

wait = True
for ite in range(2*q):
    if wait:
        k = int(input())
        wait = False
    else:
        ks = list(map(int, input().split()))
        m = 0; n = 1; ans = 0
        while m != len(ks):
            u = ks[m]
            while n != len(ks):
                v = ks[n]
                ans += crunch(u,v,index)
                n += 1
            m += 1; n = m + 1
        print(ans%(10**9 + 7))
        wait = True
#print('running time =', (time.clock()-x))
