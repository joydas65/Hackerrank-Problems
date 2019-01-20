for _ in range(int(input())):
    
    x = int(input())
    
    ans = 0
    
    z = 0
    
    n = x
    
    while x != 0:
        
        x //= 2
        
        z += 1
        
    ans = (2 ** z) - n - 1
    
    print(ans)
