def levelOrder(root):
    nxt = [];
    nxt.append(root)
    while len(nxt) > 0:
        tmp = []
        for i in range(len(nxt)):
            root = nxt[i]
            if root.left:
                tmp.append(root.left)
                if root.left.data == v1 or root.left.data == v2:
                    print(root.data)
                    break
                  
            if root.right:
                tmp.append(root.right)
                if root.right.data == v1 or root.right.data == v2:
                    print(root.data)
                    break
        nxt = tmp * 1