#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def encrypt(string):
    ans = str()
    for char in string:
        if char.isupper():
            char = rotate(char.lower())
            ans += char.upper()
        elif ord(char) >= 97 and ord(char) <= 122:
            char = rotate(char)
            ans += char
        else:
            ans += char
    return ans
        
def rotate(char):
    pos = ord(char)
    new_pos = pos + key
    if new_pos > 122:
        overflow = key%26
        new_pos = overflow + pos
        if new_pos > 122:
            new_pos = new_pos - 123 + 97
    return chr(new_pos)
    
if __name__ == '__main__':
    input()
    string = input()
    key = int(input())
    ans = encrypt(string)
    print(ans)