#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def meddle(string):
    string = "*" + string
    if len(string) % 2:
        n = len(string) // 2 + 1
    else:
        n = len(string) // 2
    ans = 0
    for i in range(1,n):
        a = string[i]
        b = string[-i]
        if  a != b:
            ans += abs(ord(a) - ord(b))
    print(ans)   
            
if __name__ == "__main__":
    n = int(input())
    for cycles in range(n):
        string = input()
        meddle(string)