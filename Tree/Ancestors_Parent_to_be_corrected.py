def lca(root,v1,v2):
    class n_root:
        def __init__(self,root,left,right):
            self.root = root
            self.left = left
            self.right = right
            self.stack = None 
    root = n_root(root,root.left,root.right)
    root.stack = [root];nxt = []
    nxt.append(root); ans = []  

    while len(nxt) > 0:  
        tmp = []
        for i in range(len(nxt)):
            root = nxt[i]
            if root.left:	
                if root.left.data == v1 or root.left.data == v2:
                    ans.append(root)
                    root.left = None
                else:
                    root.left = n_root(root.left,root.left.left,root.left.right)
                    root.left.stack = root.stack*1
                    root.left.stack.append(root.left)
                if len(ans) == 2:
                    nxt = []
                    break
                tmp.append(root.left)
         
            if root.right:
                if root.right.data == v1 or root.right.data == v2:
                    ans.append(root)
                    root.right = None
                else:
                    root.right = n_root(root.right,root.right.left,root.right.right)
                    root.right.stack = root.stack * 1
                    root.right.stack.append(root.right)
                if len(ans) == 2:
                    nxt = [];
                    break
                tmp.append(root.right)
         
        if len(ans) != 2:
            nxt = tmp * 1
            
    Root_dp = ans.pop(); Root_shl = ans.pop()
    j = Root_dp.stack; i = Root_shl.stack
    while len(j) != len(i):
        j.pop()
    root_1 = j.pop(); root_2 = i.pop()
    root_1 = root_1.root; root_2 = root_2.root
    while root_1.data != root_2.data and len(j) > 0 and len(i) > 0:
        root_1 = j.pop(); root_2 = i.pop()
        root_1 = root_1.root; root_2 = root_2.root
    return root_1