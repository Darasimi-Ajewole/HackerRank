def preOrder(root):
    ans = str(root.data)
    skipped = []
    while root:
        if root.left and root.right:
            skipped.append(root.right)
            root = root.left
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            if len(skipped):
                root = skipped.pop()
            else:
                break
        ans = ans + ' ' + str(root.data)
    print(ans)