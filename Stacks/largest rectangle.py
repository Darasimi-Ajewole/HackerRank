def largereg(arr):
    i = 0; j = 0;max_area = 0; length = len(arr)
    while i < length:
        new_h = int(arr[i]) #Present value
        new_area = [new_h,new_h,new_h]
        if new_h<1 or new_h>10**6:
            raise ValueError
        if i+1 < length:    #left of present value
            counter = 1
            k = i
            while k+1 < length:
                if min(new_h,int(arr[k+1])) == new_h:
                    new_area[1] = new_h * (counter+1)
                    counter += 1
                    k += 1
                else:
                    break
            max_area = max(max_area,new_area[1])
            
        if j:   #Right of present value
            counter = 1
            k = j
            while k:
                if min(new_h,int(arr[k-1])) == new_h:
                    new_area[2] = new_h * (counter+1)
                    counter +=1
                    k -=1
                else:
                    break
            max_area = max(max_area,new_area[2])
            
        if j and i+1 < length:
            if  min(new_h,int(arr[i-1]),int(arr[i+1])) == new_h: 
                "Wait naah"
                ans = new_area[2] + new_area[1] - new_area[0]
                max_area = max(max_area,ans)
        i += 1; j += 1
    print(max_area)

if __name__ == "__main__":
    n = int(input())
    if n<1 or n>10**5:
        raise ValueError
    arr = input().split()
    if len(arr) == n:
        largereg(arr)
