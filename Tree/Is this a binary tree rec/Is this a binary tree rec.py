def check_binary_search_tree_(root):
    inc = [-1]
    def inorder(tree,inc):
        if 1:
            if tree.left and len(inc):
                inorder(tree.left,inc)
            if len(inc) and tree.data > inc[0]:
                inc[0] = tree.data        
            else:
                inc.pop();
            if tree.right and len(inc):
                inorder(tree.right,inc)
    inorder(root,inc)
    if len(inc):
        return True
    else:
        return False