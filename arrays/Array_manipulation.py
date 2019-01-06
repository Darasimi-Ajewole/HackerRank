#-*-coding:utf8;-*-
#qpy:3
#qpy:console

Nq = input().split()
N = int(Nq[0]); q = int(Nq[1]); ans = set(); adder = 0; exc = {}
N = [0] * N; Max = 0; index = {}; exception = 0; delete = []
while q:
    queries = input().split()
    a = int(queries[0]) - 1; b = int(queries[1]) - 1; k =  int(queries[2])
    if a != b:
        if not (N[a]):    N[a] = [str(q)]
        else:    N[a].append(str(q))
        if not (N[b]):    N[b] = [str(q)]
        else:    N[b].append(str(q))
        index[str(q)] = k
    else:
        exc[a] = k
    q -= 1
for i,lst in enumerate(N):
    if lst:
        for b in lst:
            if b not in ans:
                adder += index[b]; ans.add(b)
            else:
                ans.remove(b); delete.append(b)
    if i in exc:
        exception = exc[i]; adder += exc[i];
    if adder > Max:
        Max = adder
    if len(delete):
        for i in delete:
            adder -= index[i]
        delete = []
    if exception:
        adder -= exception; exception = 0
print(Max)
