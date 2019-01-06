class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

def val(M1,M2,ans):
    S = (((M1 & M2) ^ (M1 | M2)) & (M1 ^ M2))
    if S > ans:
        ans = S
    return ans

def Max_value(A,ans):
    init = A[0]
    preys = Stack(); preys.push(init);
    i = 1
    while i < len(A):
        kiler = A[i]
        while preys.is_empty() == False:
            prey = preys.peek(); 
            ans = val(prey,kiler,ans)
            if prey <= kiler:
                break
            else:
                preys.pop() #prey killed
        preys.push(kiler) #killer becomes part of the prey to test itself
        i += 1
    print(ans)
            
N = int(input())
A = list(map(int, input().split()))
if len(A) <= N:
    ans = 0
    Max_value(A,ans)
    
                        
                
