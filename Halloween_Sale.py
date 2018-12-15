p,d,m,s = map(int, input().split())

ans = 0

while s >= p:
    
    ans += 1
    
    if p <= m:
    
        s -= p
        
    elif p > m:
        
        s -= p
        
        p -= d
        
    if p <= m:
        
        p = m
    
print(ans)
