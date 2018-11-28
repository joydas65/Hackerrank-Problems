n = int(input())

arr = list(map(int, input().split()))

d = dict()

for i in arr:
    
    d[i] = 0
    
for i in range(n):
    
    d[arr[i]] = i
    
arr = sorted(arr)

loss = arr[-1]

for i in range(1,n):
    
    if d[arr[i]] < d[arr[i-1]]:
        
        loss = min(loss,arr[i] - arr[i-1])
        
print(loss)
