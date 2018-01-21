def inOrder(root):
    skipped = []; ans = []
    while root:       
        if root.left:
            skipped.append(root)
            root = root.left
        elif root.right:
            ans.append(str(root.data))
            root = root.right
        else:
            ans.append(str(root.data))
            if len(skipped):
                root = skipped.pop()
                if root.right:
                    ans.append(str(root.data))
                    root = root.right
                else:
                    root.left = None
            else:
                break
    answer = ans[0]
    for i in range(1,len(ans)):
        answer = answer + ' ' + ans[i]
    print(answer)