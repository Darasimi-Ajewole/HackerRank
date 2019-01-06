def height(root):
    skipped = []; ans = []; i = 0
    while root:
        i += 1       
        if root.left and root.right:
            skipped.append(root.right)
            skipped.append(i)
            root = root.left
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            ans.append(i)
            if len(skipped):
                i = skipped.pop()
                root = skipped.pop()
            else:
                break
    return (max(ans)-1)