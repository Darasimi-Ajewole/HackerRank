#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def ReversePrint(head):
    lst = []; N = 0
    while head:
        lst.append(head.data); N += 1; head = head.next
    tmp = [print(lst[ite]) for ite in range(-1,-N-1,-1) ]