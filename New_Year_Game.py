for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    mods = [i%3 for i in arr]
    
    d = dict()
    
    d[1],d[2] = 0,0
    
    for i in mods:
        
        if i in d:
            
            d[i] += 1
    
    if d[1]&1 | d[2]&1:
        
        print("Balsa")
        
    else:
        
        print("Koca")
