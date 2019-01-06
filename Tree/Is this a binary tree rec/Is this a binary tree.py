def check_binary_search_tree_(root):
    skipped = []; ans = -1
    while root and ans:       
        if root.left:
            skipped.append(root)
            root = root.left
        elif root.right:
            if root.data > ans:
                ans = root.data
                root = root.right
            else:
                ans = False
                break
        else:
            if root.data > ans:
                ans = root.data
            else:
                ans = False
                break
            while len(skipped):
                root = skipped.pop()
                if root.right:
                    if root.data > ans:
                        ans = root.data
                        root = root.right
                        break
                    else:
                        ans = False
                        break
                elif root.left:
                    if root.data > ans:
                        ans = root.data
                    else:
                        ans = False
                        break                          
            else:
                break
    if ans:
        return True
    else:
        return False