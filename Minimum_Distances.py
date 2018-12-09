n = int(input())

arr = list(map(int, input().split()))

s = set()

d = dict()

for i in range(n):
    
    if arr[i] not in s:
        
        d[arr[i]] = []
        
        d[arr[i]].append(i)
        
    else:
        
        d[arr[i]].append(i)
        
    s.add(arr[i])
    
x = 0

k = 1001
    
for i in d.keys():
    
    x = len(d[i])
    
    if x > 1:
        
        for j in range(1,x):
            
            k = min(k,d[i][j] - d[i][j-1])

print(k)
