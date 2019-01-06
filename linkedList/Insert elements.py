#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def Insert(head, data):
    main = head
    if head:
        while head.next:
            head = head.next
        head.next = Node(data,None)
    else:
        main = Node(data,None)
    return main