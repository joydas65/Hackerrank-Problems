n,k = map(int, input().split())

arr = list(map(int, input().split()))

d = dict()

for i in range(0,k):
    
    d[i] = []
    
for i in arr:
    
    d[i%k].append(i)
    
ans = 0

if len(d[0]) > 0:
    
    ans += 1
    
for i in range(1,(k//2)+1):
    
    if i != (k - i):
        
        if len(d[i]) > len(d[k - i]):
            
            ans += len(d[i])
            
        else:
            
            ans += len(d[k - i])
            
    else:
        
        ans += 1
        
print(ans)
