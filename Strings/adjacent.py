#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def alternate(string):
    a = string[0]
    ans = 0
    for i in range(1,len(string)):
        b = string[i]
        if b == a:
            ans += 1
        else:
            a = b
    print(ans)

if __name__ == "__main__":
    n = int(input())
    for cycle in range(n):
        string = input()
        alternate(string)