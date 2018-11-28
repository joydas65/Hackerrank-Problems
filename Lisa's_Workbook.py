n,k = map(int, input().split())

arr = list(map(int, input().split()))

pageNumber = 1
    
special = 0
    
for i in range(n):
        
    temp = arr[i]
        
    lb = 1
        
    ub = k
        
    while temp - k >= 0:
            
        if pageNumber >= lb and pageNumber <= ub:
                
            special += 1
                
        temp -= k
        
        pageNumber += 1
        
        if temp == 0:
            
            break
            
        lb = ub + 1
            
        ub += k
        
    if temp > 0:
            
        ub = (ub - k) + temp

        if pageNumber >= lb and pageNumber <= ub:

            special += 1

        pageNumber += 1
        
print(special)
