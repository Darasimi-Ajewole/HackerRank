#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def InsertNth(head, data, position):
    counter = 1; main = head
    if position == 0:
        head = Node(data,head); return head
    else:
        begin = head;end = head.next; 
        while counter != position:
            begin = end; end = end.next
            counter += 1
        begin.next = Node(data,end); return main