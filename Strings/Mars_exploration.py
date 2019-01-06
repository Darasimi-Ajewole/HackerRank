#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def filter_out():
    ans = 0
    blocks = int(len(string)/3)
    for i in range (1,blocks+1):
        n = i * 3
        part = string[n-3:n]
        if part[0] != 'S':
            ans += 1
        if part[1] != 'O':
            ans += 1
        if part[2] != 'S':
            ans += 1
    print(ans)    
    
if __name__ == '__main__':
    string = input()
    filter_out()