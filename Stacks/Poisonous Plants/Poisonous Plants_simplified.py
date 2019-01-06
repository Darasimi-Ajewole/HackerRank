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
    def element(self):
        return print(self.items)

def your_kill(P_Stack,killer,DC):
    days = 0
    while P_Stack.size() > 0 and P_Stack.peek() > killer:
        P_Stack.pop(); killed_DC = DC.pop()
        days += 1
        if killed_DC > days:
            days = killed_DC
    P_Stack.push(killer)
    DC.push(days)
    return days
        

def poisonous(arr):
    i = len(arr) - 1; DC = Stack(); P_stack = Stack(); ans = [] #DC: Death Count
    while i >= 0:
        if P_stack.is_empty():
            P_stack.push(arr[i])
            DC.push(0)
        else:
            temp = your_kill(P_stack,arr[i],DC)
            ans.append(temp)
        i -= 1
    print(max(ans))

if __name__ == "__main__":
    n = int(input())
    if n<1 or n>10**5:
        raise ValueError
    temp_arr = input().split()
    arr = []
    for i in range(len(temp_arr)):
        temp = int(temp_arr[i])
        if temp < 0 or temp > 10**9:
            raise ValueError
        arr.append(temp)
    if len(arr) == n:
        poisonous(arr)
