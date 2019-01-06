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
    
def poisonous(arr,no_of_days):
    Empty = []; next_arr = Empty*1; length = len(arr); i = 0;
    P_stack = Stack(); 
    while i < length:
        if P_stack.is_empty() or arr[i] >= P_stack.peek():
            P_stack.push(arr[i])
            next_arr.append(arr[i])
        elif P_stack.peek() > arr[i]:
            P_stack.pop()
            next_arr.pop()
            P_stack.push(arr[i])
            next_arr.append(arr[i])
        i += 1
    if length == len(next_arr):
        return print(no_of_days)
    else:
        no_of_days += 1
        poisonous(next_arr,no_of_days)
    

if __name__ == "__main__":
    n = int(input())
    if n<1 or n>10**5:
        raise ValueError
    temp_arr = input().split()
    no_of_days = 0
    arr = []
    for i in range(len(temp_arr)):
        temp = int(temp_arr.pop())
        if temp < 0 or temp > 10**9:
            raise ValueError
        arr.append(temp)
    if len(arr) == n:
        poisonous(arr,no_of_days)
