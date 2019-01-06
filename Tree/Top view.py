def topView(root):
    skipped = []; ans = [];
    if root.left:
        while root:
            if root.left:
                skipped.append(root)
                root = root.left
            elif len(skipped):
                ans.append(str(root.data))
                root = skipped.pop()
                root.left = None
            else:
                break
    if root.right:
        ans.append(str(root.data))
        root = root.right
        while root:
            ans.append(str(root.data))
            if root.right:
                root = root.right
            else:
                break
   
    answer = ans[0]
    for i in range(1,len(ans)):
        answer = answer + ' ' + ans[i]
    print(answer)