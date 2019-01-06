#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def check(string):
    queue = str()
    wanted = "010"
    ans = 0
    for char in string:
        if len(queue) < 3:
            queue += char
        else:
            if queue == wanted:
                ans += 1
                queue = char
            else:
                queue = queue[1:] + char
        
    print(ans)
if __name__ == "__main__":
    input()
    string = input() + "*"
    check(string)