#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def index(x,l,N):
    return ((x^l)%N)
N_Q = input().split()
N = int(N_Q[0]); Q = int(N_Q[1]); 
l = 0; Arr = [ [] for i in range(N) ]
while Q:

    q = list(map(int, input().split()))
    
    i = index(q[1],l,N); tmp = Arr[i]
    if q[0] == 1:
        tmp.append(q[2]);
        
    else:
        y = q[2] % len(tmp)
        l = tmp[y]; print(l)
    Q -= 1