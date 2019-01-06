def insert(r,val):
    if r:    
        if r.data > val:
            r.left = insert(r.left,val)
        else:
            r.right = insert(r.right,val)     
    else:
        r = Node('')
        r.data = val
        r.right = None
        r.left = None
    return r