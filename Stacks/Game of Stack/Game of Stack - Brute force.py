def load_useful(Stack,arr,limit): #loading Stack
    i = 0; Sum = 0
    while i < len(arr):
        Sum += int(arr[i])
        if Sum > limit:
            Sum -= int(arr[i])
            break
        Stack.append(int(arr[i]))
        #if Stack.peek() < 0  or Stack.peek() > 10**6:
            #raise ValueError
        i+=1
    Stack.append(Sum);
    return Stack

def more_element(S1,S2): #Stack with more element
    if len(S1) == max(len(S1),len(S2)):
        return S1
    elif len(S2) == max(len(S1),len(S2)):
        return S2
    elif len(S1) == len(S2):
        if S1[len(S1) - 1] < S2[len(S2) - 1]: #S1.[len(S1) - 1] will return sum of element in S1, same with S2
            return S1
        else:
            return S2
    
def Max_Pick(S1,S2,limit): 
    S = more_element(S1,S2); Size = [];
    if len(S) == len(S1):
        Sum_1= S.pop(); Sum_2 = S2.pop(); padding = 000; size = len(S)
        S.append(padding)
        for n in range(size):
            Sum_1 -=S.pop(); temp_Sum = Sum_1; temp_arr = S*1; #print(temp_Sum)
            for el in range(len(S2)):
                temp_arr.append(S2[el])
                temp_Sum += S2[el]
                if temp_Sum > limit:
                    temp_Sum -= S2[el]
                    temp_arr.pop()
                    break
            Size.append(len(temp_arr))
                   
        if len(Size) == 0:
            print('0')
        else:
            print(max(Size))
    else:
        Max_Pick(S2,S1,limit)

if __name__ == "__main__":
    g = int(input()) #number of games
    if g < 1 or g > 50:
        raise ValueError
    for i in range(g):
        lst = input().split()  #List of number of integers in stack A and B, including the limiting number 
        n = int(lst[0]); m = int(lst[1]); x = int(lst[2])
        if min(n,m)<1 or max(n,m)>10**5 or x < 1  or  x > 10**9:
            raise ValueError
            
        arr1 = input().split()  #Stack A element
        arr2 = input().split()  #Stack B element
        if len(arr1) != n or len(arr2) != m:
            raise ValueError
        
        Stack_A = [];   Stack_B = [];
        load_useful(Stack_A,arr1,x); load_useful(Stack_B,arr2,x);
        Max_Pick(Stack_A,Stack_B,x);