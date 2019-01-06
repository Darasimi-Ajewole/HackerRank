class root:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
    def insert(self,item,tag):
        if tag == 'a':
            self.left = item
        else:
            self.right = item
    
def levelOrder(root,k):
    nxt = [];
    nxt.append(root)
    i = 1
    if i == k:
        return [root]
    else:
        while len(nxt) > 0:
            tmp = []
            for m in range(len(nxt)):
                root = nxt[m]
                if root.left:
                    tmp.append(root.left)
                if root.right:
                    tmp.append(root.right)
            i += 1
            if k == i:
                return tmp
                nxt = []
            elif len(tmp):
                nxt = tmp * 1
            else:
                return tmp
    
    
def Swap(root):
    if root.left and root.right:
        root.left, root.right = root.right,root.left
    elif root.left:
        root.right = root.left
        root.left = None
    else:
        root.left = root.right
        root.right = None

def inOrder(root):
    skipped = []; ans = []
    while root:       
        if root.left:
            skipped.append(root)
            root = root.left
        elif root.right:
            ans.append(str(root.key))
            root = root.right
        else:
            ans.append(str(root.key))
            while len(skipped):
                root = skipped.pop()
                if root.right:
                    ans.append(str(root.key))
                    root = root.right
                    break
                elif root.left:
                    ans.append(str(root.key))
                    
                    
            else:
                break
    answer = ans[0]
    for i in range(1,len(ans)):
        answer = answer + ' ' + ans[i]
    print(answer)

N = int(input())
Tree = root(1)
lst = [Tree];

for i in range(N):
    Node = lst[i]
    ab = list(map(int, input().split()))
    if ab[0] == -1:
        "do nothing"
    else:
        temp1 = root(ab[0])
        Node.insert(temp1,'a')
        lst.append(temp1)
        
    if ab[1] == -1:
        "do nothing"
    else:
        temp2 = root(ab[1])
        Node.insert(temp2,'b')
        lst.append(temp2)   

T = int(input())
for ite in range(T):
    k = int(input())
    i = 1
    while 7:
        H = levelOrder(Tree,i*k)
        if len(H) == 0:
            break
        for j in H:
            Swap(j)
        i += 1
    inOrder(Tree)