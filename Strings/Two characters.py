#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def del_red(string):    #delete redundant
    death_row = set()
    index = {}
    counter = {}
    prev = None
    for i,char in enumerate(string):
        if char == prev:
            death_row.add(char)
        
        elif char not in index:
            index[char] = [i]
      
        else: 
            index[char].append(i)
        prev = char
    
    for char in index:
        count = len(index[char])
        if count == 1:
            death_row.add(char)
        elif char not in death_row:
            if count not in counter:
                counter[count] = [char]
            else:
                counter[count].append(char)
    
    [index.pop(char, None) for char in death_row ]
    return (index, counter)

def arrange():
    tried = {}
    for counts in counter:
        _list = counter[counts]
        for i,char in enumerate(_list):
            for k in range(i + 1, len(_list)):
                match(char,_list[k])
        merge_1 = str(counts) + str(counts - 1)
        merge_2 = str(counts) + str(counts + 1)
        
        if merge_1 not in tried:
            pner_1 = counter.get(counts - 1,[])
            for char in _list:
                for char_2 in pner_1:
                    match(char, char_2)
            tried[merge_1] = None    
        
        if merge_2 not in tried:
            pner_2 = counter.get(counts + 1,[])
            for char in _list:
                for char_2 in pner_2:
                    match(char,char_2)
            tried[merge_2] = None

def match(char, char_2):
    pos_1 = index[char]
    pos_2 = index[char_2]
    if pos_1[0] < pos_2[0]:
        start = pos_1
        next = pos_2
    else:
        start = pos_2
        next = pos_1
   
    minimum = min(len(start), len(next))
    total = len(start) + len(next)
    global ans
    tmp = ans
    x = 0
    if ans < total:
        ans = total
    
    if len(next) > len(start):
        ans = tmp
        
    else:    
        for i in range(1,minimum):
            if start[i] > next[i] or start[i] < next[i - 1]:
                ans = tmp
                break
            """
            #print("***",ans,start, '\n' , next)
            x  = 1
            break
    if not x:
        print("***",ans,start, '\n' , next)
"""    
    
if __name__ == '__main__':
    input()
    string = input()
    ans = 0
    index,counter = del_red(string)
    arrange()
    if len(string) == 2:
        print(2)
    else:
        print(ans)