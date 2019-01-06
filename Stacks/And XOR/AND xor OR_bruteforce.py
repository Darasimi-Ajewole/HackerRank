def val(M1,M2,ans):
    S = (((M1 & M2) ^ (M1 | M2)) & (M1 ^ M2))
    if S > ans:
        ans = S
    else:
        "Change nothing"
    return ans

def Max_value(A,ans):
    i = 0
    while i < len(A) - 1:
        M1 = A[i]
        j = i + 1
        M2 = A[j]
        ans = val(M1,M2,ans)
        lst = M2              #Least number after M1
        j += 1
        while j < len(A):
            M2 = A[j]
            if M1 < M2 and M2 > lst:
                j += 1
                continue
            elif M1 < M2 and M2 < lst:
                ans = val(M1,M2,ans)
                lst = M2
            else:
                break
            j += 1
        i += 1
    print(ans)
    
            
            
N = int(input())
A = list(map(int, input().strip().split(' ')))
if len(A) <= N:
    ans = 0
    Max_value(A,ans) 