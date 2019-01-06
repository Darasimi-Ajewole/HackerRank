class root:
    def __init__(self,key,depth):
        self.key = key
        self.left = None
        self.right = None
        self.depth = depth
        
    def insert(self,item,tag):
        if tag == 'a':
            self.left = item
        else:
            self.right = item

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
Tree = root(1,1)
lst = [Tree]; 
H = [0,[Tree]]            # 0 is just padding

for i in range(N):
    Node = lst[i]
    
    ab = list(map(int, input().split()))
    if ab[0] == -1:
        "do nothing"
    else:
        temp = root(ab[0],Node.depth + 1)
        lst.append(temp)
        
        if (Node.depth + 1) >= len(H):
            temp_lst = []
            H.append(temp_lst)
        else:
            temp_lst = H[Node.depth + 1]
        
        temp_lst.append(temp)
        Node.insert(temp,'a')
    if ab[1] == -1:
        "do nothing"
    else:
        temp = root(ab[1], Node.depth + 1)
        lst.append(temp)
        
        if (Node.depth + 1) >= len(H):
            temp_lst = []
            H.append(temp_lst)
        else:
            temp_lst = H[Node.depth + 1]
        
        
        temp_lst.append(temp)
        Node.insert(temp,'b')

T = int(input())
for ite in range (T):
    k = int(input())
    i = 1
    while i * k < len(H):
        temp = H[i*k]
        for j in temp:
            Swap(j)
        i += 1
    inOrder(Tree)
    #answer = str(ans[0])
    #for i in range(1,len(ans)):
        #answer = answer  + ' ' + str(ans[i])
    #print(answer)
