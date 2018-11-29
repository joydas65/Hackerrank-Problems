n = int(input())

arr = list(map(int, input().split()))

d = dict()
    
for i in range(n):
    
    d[arr[i]] = i
    
x = arr.copy()

x = sorted(x)
    
i = n - 1

ans = 0

while i >= 0:
    
    if arr[i] == x[i]:
        
        i -= 1
        
        continue
    
    arr[d[x[i]]],arr[i] = arr[i],arr[d[x[i]]]
    
    d[arr[d[x[i]]]] = d[x[i]]
    
    d[x[i]] = i
    
    i -= 1
    
    ans += 1
    
print(ans)
    
    
    
    
