#-*-coding:utf8;-*-
#qpy:3
#qpy:console

def super_reduce(initial_string):
    reducer = []
    for char in initial_string:
        if not len(reducer):
            reducer.append(char)
        elif char == reducer[-1]:
            reducer.pop()
        else:
            reducer.append(char)
    if len(reducer): 
        return "".join(str(x) for x in reducer)
    else:
        return "Empty String"

if __name__ == '__main__':
    initial_string = input()
    print(super_reduce(initial_string))