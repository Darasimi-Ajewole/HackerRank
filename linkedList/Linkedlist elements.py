#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)