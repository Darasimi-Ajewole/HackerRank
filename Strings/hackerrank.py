#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def find_string(string):
    ans = ["h","a","c","k","e","r","r","a","n","k"]
    ans.reverse()
    next_char = ans[-1]
    for char in string:
        if char == next_char:
            ans.pop()
            if not(len(ans)):
                print("YES")
                break
                
            else:
                next_char = ans[-1]
            
    if len(ans):
        print("NO")     
         
if __name__ == "__main__":
    n = int(input())
    for j in range(n):
        string = input()
        find_string(string)