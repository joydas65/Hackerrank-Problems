n,k = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)

x = 0

l = len(arr)

transmitter = 0

while x < l:
    
    val = arr[x] + k
    
    while x < l and arr[x] <= val:
        
        x += 1
        
    x -= 1
    
    transmitter += 1
    
    val = arr[x]
    
    while x < l and arr[x] <= val + k:
        
        x += 1
        
print(transmitter)
