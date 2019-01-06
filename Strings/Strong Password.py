#-*-coding:utf8;-*-
#qpy:3
#qpy:console

spec_char = {"!","@","""#""",
            "$","%","^","&",
            "*","(",")","-","+"}
            
def is_upper(char):
    return char.isupper()

def is_lower(char):
    return char.islower()

def is_digit(char):
    return char.isdigit()

def is_special(char):
    return char in spec_char

def is_long(string):
    if len(string) >= 6: return 0
    else:
        return 6 - len(string)
        
def strengthen(string):
    for char in string:
        if not len(conditions):
            break
        for num in conditions:
            func = conditions[num]
            if func(char):
                conditions.pop(num)
                break
    unfulfilled = len(conditions)
    shortage = is_long(string)
    return max(unfulfilled, shortage)      
    
conditions = {
	    1: is_upper,
	    2: is_lower,
	    3: is_digit,
	    4: is_special,
	}
	
    
if __name__ == '__main__':
    input()
    string = input()
    print (strengthen (string))