#-*-coding:utf8;-*-
#qpy:3
#qpy:console

string = input()
interest = { i for i in range(97,123) }
for char in string:
    if char.isupper():
        char = char.lower()
    interest.discard(ord(char))
    
if not len(interest):print("pangram")
else: print("not pangram")