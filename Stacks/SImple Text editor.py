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
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def Carry_out(new,S,undo):
    if new[0] == "1":
        if undo:
            undo.push(new)
        Str = new[1]
        new_str = ''
        for i in range(len(Str)):
            if (ord(Str[i]) - 97) >= 0 and (122- ord(Str[i])) >= 0:
                new_str += Str[i]
        S += new_str
        return S
        
    elif new[0] == "2":
        k = int(new[1]); Lth = len(S)
        if Lth >= k:
            thresh = Lth - k; new[1] = S[thresh:]; S = S[0:thresh]
            if undo:
                undo.push(new)
        return S
    
    elif new[0] == "3":
        k = int(new[1]) - 1
        print(S[k])
        return S

    else:
        if undo.size() > 0:
            new  = undo.pop()
            if new[0] == "1":
                new[0] = "2"; new[1] = len(new[1])
                S = Carry_out(new,S,False)
                return S
            else:
                new[0] = "1";  S = Carry_out(new,S,False); return S
        
N = int(input())
S = ""; undo = Stack()
for i in range(N):
    new_instr = input().split()
    S = Carry_out(new_instr,S,undo)
