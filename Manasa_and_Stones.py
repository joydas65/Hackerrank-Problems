import math

for _ in range(int(input())):
    
    n = int(input())
    
    a = int(input())
    
    b = int(input())
    
    d = abs(b - a)
    
    lb = (n - 1)*a
    
    ub = (n - 1)*b
    
    lb,ub = min(lb,ub),max(lb,ub)
    
    while lb <= ub:
        
        print(lb,end = " ")
        
        lb += d

        if d == 0:

            break
        
    print()
