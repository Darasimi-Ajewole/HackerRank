#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def cal_wei(char):
    return ord(char) - 96
    
def find_sub(string):
    first_char = string[0]
    checker = [first_char]
    ans = set()
    ans.add(cal_wei(first_char))
    
    for char in string[1:]:
        if char ==  checker[-1]:
            checker.append(char)
            n = len(checker) * cal_wei(char)
            ans.add(n)
        else:
            ans.add(cal_wei(char))  
            checker = [char]
    return ans  
       
if __name__ == "__main__":
    string = input()
    n = int(input())
    ans = find_sub(string)
    #print(ans)
    for i in range(n):
        q = int(input())
        if q in ans:
            print("Yes")
        else:
            print("No")
