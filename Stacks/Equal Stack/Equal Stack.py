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
    def element(self):
        return print(self.items)

def load(Stack,arr,n):
    i = 0; h = 0
    while i < n:
        Stack.push(int(arr.pop()))
        if Stack.peek() < 0 or Stack.peek() > 100:
            raise ValueError
        h += Stack.peek(); i+=1
    Stack.push(h) #Height of stack would be on top of the stack
    return Stack

def greatest(S1,S2,S3):
    h = max(S1.peek(),S2.peek(),S3.peek())
    if S1.peek() == h:
        return S1
    elif S2.peek() == h:
        return S2
    else:
        return S3
def Max_height(S1,S2,S3):
    h1 = S1.peek(); h2 = S2.peek(); h3 = S3.peek(); not_equal = True
    while not_equal:
        if h1==h2==h3:
            print(h3)
            break
        S = greatest(S1,S2,S3)
        if S.size() == 2:
            print('0')
            break
        H = S.pop()
        S.push(H - S.pop())
        h1 = S1.peek(); h2 = S2.peek(); h3 = S3.peek()

    
    
if __name__ == "__main__":
    n = input().split()
    n1 = int(n[0]); n2 = int(n[1]); n3 = int(n[2])
    if min(n1,n2,n3)<0 or max(n1,n2,n3)>10**5:
        raise ValueError

    arr1 = input().split()
    arr2 = input().split()
    arr3 = input().split()
    if len(arr1) != n1 or len(arr2) != n2 or len(arr3) != n3:
        raise IndexError
        
    Stack1 = Stack();Stack2  = Stack();Stack3 = Stack()
    load(Stack1,arr1,n1); load(Stack2,arr2,n2); load(Stack3,arr3,n3)
    Max_height(Stack1,Stack2,Stack3)    
