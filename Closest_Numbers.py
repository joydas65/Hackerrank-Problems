n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

val = (10 ** 7) + 1

d = dict()

for i in range(1,n):
    
    d[abs(arr[i]-arr[i-1])] = []
    
for i in range(1,n):
    
    d[abs(arr[i]-arr[i-1])].append((arr[i-1],arr[i]))
    
for i in range(1,n):
    
    val = min(val,abs(arr[i]-arr[i-1]))
    
x = []
    
for i in d.keys():
    
    if i == val:
        
        x = d[i]
        
        break
        
for i in x:
    
    print(i[0],i[1],end = " ")
