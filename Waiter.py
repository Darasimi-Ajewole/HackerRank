def iPrime(i,prime,dividers):
    if i < len(prime):
        return prime[i]
    else:
        multi = prime[-1]//i-1
        nxt = i*multi
        if nxt < prime[-1]:
            nxt = prime[-1] + 2
        else:
            if nxt%2 == 0:
                nxt += 1
        detected = False
        while not detected:
            for j in dividers:
                if nxt%j == 0:
                    nxt += 2
                    break
                elif nxt//j <= 1:
                    detected = True
                    dividers.append(nxt)
                    prime.append(nxt)
                    return nxt
    
def Arrange(A,Q):
    i = 1; prime = [1,2,3,5,7,11,13]
    dividers = [3,5,7,11,13]
    while i <= Q:
        p = iPrime(i,prime,dividers); Aq = []
        for j in range(len(A)):
            N = A[j]
            if N%p == 0:
                print(N)
            else:
                Aq.append(N)
        A = Aq * 1
        A.reverse()
        i = i + 1
    for j in range(len(Aq)):
        print(Aq[j])
        
    

N_Q = input().split()
Q = int(N_Q[1])
A = list(map(int, input().split()))
Arrange(A,Q)

