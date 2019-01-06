#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def check_funny(string):
    s = [ord(char) for char in string ]
    r = s * 1; 
    r.reverse()
    for k in range(len(s) - 1):
        a = abs(s[k] - s[k+1])
        b = abs(r[k] - r[k+1])
        if a != b:
            print("Not Funny")
            return 
    print("Funny")
    
    
    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        check_funny(string)