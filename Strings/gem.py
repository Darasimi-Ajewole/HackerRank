#-*-coding:utf8;-*-
#qpy:3
#qpy:console

if __name__ == "__main__":
    n = int(input())
    first_string = input()
    gem = {char:None for char in first_string}
    for cycle in range(1,n):
        strings = input()
        tmp = {}
        for char in strings:
            if char in gem:
                tmp[char] = None
        gem = tmp
    print(len(gem))
            
    