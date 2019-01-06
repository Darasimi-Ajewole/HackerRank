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

def ref(S):
    if S == "}":
        ans = "{"
    elif S == "]":
        ans = "["
    elif S == ")":
        ans = "("
    return ans

def isBalanced(s):
    Pts_stack = Stack()
    num = len(s)
    if num<1 or num>10**3:
        raise ValueError
    else:
        for inp in s:
            if inp in  "{([":
                Pts_stack.push(inp)
            elif inp in "})]":
                if Pts_stack.is_empty():
                    Pts_stack.push(inp)
                    break
                if ref(inp) == Pts_stack.peek():
                    Pts_stack.pop()
                else:
                    Pts_stack.push(inp)
                    break
            else:
                raise ValueError
        if Pts_stack.is_empty():
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        isBalanced(s)
