def sortTheSubString(x):
    
    f = str()
    
    for i in "abcdefghijklmnopqrstuvwxyz":
        
        for j in x:
            
            if i == j:
                
                f = f + j
                
    return f

for _ in range(int(input())):
    
    s = input()
    
    arr,n = [],len(s)
    
    for i in range(n):
        
        j = 1
        
        while i+j <= n:
            
            if i == 0 and j == n:
                
                break
            
            arr.append(sortTheSubString(s[i:i+j]))
            
            j += 1
            
    arr = sorted(arr)
    
    d = dict()
    
    for i in arr:
        
        if i in d:
            
            d[i] += 1
            
        else:
            
            d[i] = 1
            
    ans = 0
            
    for i in d:
        
        ans += ((d[i])*(d[i]-1)//2)
        
    print(ans)
        
        
    #print(arr)
