n = int(input())

arr = list(map(int, input().split()))

odds = 0

for i in arr:
    
    if i % 2 == 1:
        
        odds += 1
        
if odds % 2 == 1:
    
    print("NO")
    
else:
    
    ans = 0
    
    for i in range(len(arr)):
        
        if arr[i] % 2 == 1:
            
            arr[i] += 1
            
            arr[i + 1] += 1
            
            ans += 2
            
    print(ans)
