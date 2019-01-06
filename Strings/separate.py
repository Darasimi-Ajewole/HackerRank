#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def seperate(string):
    start = 1
    ans = None
    if string[0] == "0":
        print("NO")
        return ans
        
    while (start <= len(string)// 2) and not ans:
        tmp = string
        first = int(tmp[:start])
        ans = first
        rest = tmp[start:]
        next = str(first + 1)
        c = len(next)
        while len(rest):
            if next != rest[:c]:
                ans = None
                break
            else:
                next = str(int(next) + 1)
                rest = rest[c:]
                c = len(next)
        start += 1
    
    if ans:
        print("YES",ans)
    else:
        print("NO")
        
if __name__ == '__main__':
    n = int(input())
    for cycles in range(n):
        string = input()
        seperate(string)