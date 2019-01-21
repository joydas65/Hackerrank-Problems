n,m = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)

ans = []

flag = 0

for i in range(n):
    
    first = 0
    
    last = m - 1
    
    middle = (first + last)//2
    
    while first <= last:
        
        if arr[middle] < i:
            
            first = middle + 1
            
        elif arr[middle] == i:
            
            ans.append(0)
            
            flag = 1
            
            break
            
        else:
            
            last = middle - 1
            
        middle = (first + last)//2
            
    if flag == 0:
        
        if first >= 0 and last >= 0 and last < m and first < m:
            
            ans.append(min(abs(arr[first]-i),abs(arr[last]-i)))
            
        elif first >= 0 and first < m:
            
            ans.append(abs(arr[first]-i))
            
        else:
            
            ans.append(abs(arr[last]-i))
        
    flag = 0
    
print(max(ans))
