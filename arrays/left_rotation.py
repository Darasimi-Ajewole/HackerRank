#-*-coding:utf8;-*-
#qpy:3
#qpy:console

N_d = input().split(); d = int(N_d[1]); 
Arr = input().split(); N = len(Arr); start = d%N
for ite in range(N):
   if start == N:
       start = 0
   print(Arr[start], end = ' ')
   
   start += 1