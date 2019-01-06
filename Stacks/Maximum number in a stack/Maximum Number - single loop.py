class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
        
        
def func(N):
    Max_stack = Stack()
    ans = 0
    ans_list = []
    chk_list = []
    temp= 0
    while N > 0:
        new_list = input().split()
        N -=1
        if int(new_list[0]) > 3 or int(new_list[0]) < 1:
            raise ValueError
        elif new_list[0] == '1':
                new_num = int(new_list[1])
                if new_num >=1 and new_num <= 10**9:
                    Max_stack.push(new_num)
                    chk_list.append(new_num)
                    if Max_stack.size() == 1:
                        ans = new_num
                    elif new_num > ans:
                        ans = new_num
                else:
                    raise ValueError
        elif new_list[0] == '2':
            if Max_stack.peek() == ans:
                temp = ans
            Max_stack.pop()
            chk_list.pop()
        elif new_list[0] == '3':
            if ans == temp:
                ans = max(chk_list)
            ans_list.append(ans)
    for i in range(len(ans_list)):
        print(ans_list[i])

N = int(input())
if N >=1 and N <=10**5:
    func(N)
else:
    raise ValueError
