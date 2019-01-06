def decodeHuff(root,s):
    ans = ''; top = root;
    for num in s:
        if num == "1":
            root = root.right
            if root.data != '\0':
                ans = ans + root.data
                root = top
        else:
            root = root.left
            if root.data != '\0':
                ans = ans + root.data
                root = top
    print(ans)