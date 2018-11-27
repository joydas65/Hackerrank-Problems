for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    d = dict()
    
    for i in arr:
        
        d[i] = 0
        
    for i in range(n):
        
        d[arr[i]] = i
        
    x = arr.copy()
    
    x = sorted(x)
    
    c = 0
    
    ind = n - 1
    
    ub = d[x[ind]]
    
    prev = ub
    
    PLAYER_NAME = "BOB"
    
    while ub >= 1:
        
        ind -= 1
        
        ub = d[x[ind]]
        
        if ub < prev:
        
            c += 1

            if c % 2 == 1:

                PLAYER_NAME = "ANDY"

            else:

                PLAYER_NAME = "BOB"
                
            prev = ub
            
    print(PLAYER_NAME)
