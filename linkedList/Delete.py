#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def Delete(head, position):
    counter = 1; main = head
    if position == 0:
        return head.next
    else:
        begin = head; middle = head.next; end = middle.next 
        while counter != position:
            begin = middle; middle = end; end = end.next
            counter += 1
        begin.next = end; return main