def postOrder(root):
    skipped = []; ans = []
    while root:
        ans.append(str(root.data))
        if root.left and root.right:
            skipped.append(root)
            root = root.right
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            if len(skipped):
                root = skipped.pop()
                root = root.left
            else:
                break
    answer = ans.pop()
    for i in range(len(ans)):
        answer = answer + ' ' + ans.pop()
    print(answer)