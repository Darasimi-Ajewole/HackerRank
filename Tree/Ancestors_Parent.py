def lca(root,v1,v2): 
    while 1:  
        if root.data > v1 and root.data > v2:
            root = root.left
        elif root.data < v1 and root.data < v2:
            root = root.right
        else:
            return root
            break