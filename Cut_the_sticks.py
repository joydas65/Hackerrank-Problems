n = int(input())

arr = list(map(int, input().split()))

n = len(arr)

x = min(arr)

ans = []

while n > 1:
    
    ans.append(n)
    
    for i in range(n):
        
        arr[i] -= x
        
    while True:
        
        if 0 in arr:
            
            arr.remove(0)
            
        else:
            
            break
            
    n = len(arr)

    if arr == []:

        break
    
    x = min(arr)
    
for i in ans:
    
    print(i)

if arr != []:
    
    print(1)
