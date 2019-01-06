#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def evaluate (_list):
    st,en,d = _list
    n = len(d)
    ans = 0
    
    for res in count:
        i = 0
        while (i + res) <= n:
            g = d[i:i+res]
            g_pos = genes.get(g,[]) 
            
            for j in g_pos:
                if j < int(st) or j > int(en):
                    break
                else:
                    ans += pos[j]
            i += 1
    return ans
    
    
                
if __name__ == "__main__":
    n = int(input())
    g = input().split(" ")
    h = input().split(" ")
    s = int(input())
    genes = {}
    pos = {}
    count = set()
    final_ans = set()
    
    for i in range(n):
        if g[i] not in genes:
            genes[g[i]] = [i]
        else:
            genes.get(g[i]).append(i)
        pos[i] = int(h[i])
        count.add(len(g[i]))
    
    _list = input().split()
    ans_1 = evaluate(_list)
    
    _list = input().split()
    ans_2 = evaluate(_list)
    
    high = max(ans_1, ans_2)
    low = min(ans_1,ans_2)
   
    for cycle in range(s - 2):
        _list = input().split()
        ans = evaluate(_list)
        if ans > high:
            high = ans
        elif ans < low:
            low = ans
 
    print(low, high)