n = int(input())

arr = list(map(int, input().split()))

d = dict()

for i in range(1,n+1):
    
    d[i] = 0
    
for i in range(n):
    
    d[arr[i]] = i + 1
    
for i in range(1,n+1):
    
    print(d[d[i]])
