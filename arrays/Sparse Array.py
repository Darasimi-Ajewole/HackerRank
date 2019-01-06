#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def query(string,S):
    if string in S:
        print(S[string])
    else:
        print(0)
N = int(input())

S = {}

for ite in range(N):
    tmp = input()
    if not tmp in S:
        S[tmp] = 1
    else:
        S[tmp] += 1;
Q = int(input());
[query(input(),S) for ite in range(Q)]