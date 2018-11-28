import math

d = dict()

for i in range(1,5*(10 ** 4)):
    
    d[i] = i ** 2
    
for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    lb = 1

    ub = 5*(10 ** 4)

    while lb <= ub:

        mid = (lb + ub)//2

        if d[mid] > a:
            
            ub = mid - 1
            
        elif d[mid] < a:
            
            lb = mid + 1
            
        else:
            
            break
            
    f = mid
    
    lb = 1
    
    ub = 5 * (10 ** 4)
    
    while lb <= ub:
        
        mid = (ub + lb)//2
        
        if d[mid] > b:
            
            ub = mid - 1
            
        elif d[mid] < b:
            
            lb = mid + 1
            
        else:
            
            break
            
    g = mid
    
    ans = 0
    
    if d[f] >= a and d[g] <= b:
        
        print(g - f + 1)
        
    elif (d[f] >= a and d[g] > b) or (d[f] < a and d[g] <= b):
        
        print(g - f)
        
    elif d[f] < a and d[g] > b:
        
        print(g - f - 1)
