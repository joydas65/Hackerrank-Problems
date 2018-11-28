n,k = map(int, input().split())

c = list(map(int, input().split()))

i = 0

ans = 100

if c[0] == 1:
    
    ans = 98

thunderclouds = 0

x = 0

while i < n:
    
    if c[(i+k)%n] == 1 and (i+k)%n != 0:
        
        thunderclouds += 1
        
    x += 1
    
    i = (i + k)%n
    
    if i == n - 1:
        
        x += 1
        
        break
        
    if i == 0:
        
        break
        
print(ans - (thunderclouds * 2) - x)
