level = {}
for i in range(6): 
    level[i] = list(map(int,input().split()))
ans = []; i = 0; j = 0; ite = 16
while ite:
    tmp = []
    if i != 4:
        top = level[j]; mid = level[j+1];bottom = level[j+2]
        tmp.append(sum(top[i:i+3])); tmp.append(mid[i+1]); tmp.append(sum(bottom[i:i+3]))
        ans.append(sum(tmp)); i += 1; ite -= 1
     
    else:
    
        j+=1; i = 0;
print(max(ans))