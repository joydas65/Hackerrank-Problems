for _ in range(int(input())):
    
    n,c,m = map(int, input().split())
    
    ans = n//c
    
    wrappers = ans
    
    no_of_wrappers_given,no_of_chocolates_got = 0,0
    
    while wrappers >= m:
        
        ans += (wrappers // m)
        
        no_of_wrappers_given = m*(wrappers // m)
        
        no_of_chocolates_got = (wrappers // m)
        
        wrappers -= no_of_wrappers_given
        
        wrappers += no_of_chocolates_got
        
    print(ans)
