n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr,reverse = True)

i = 0

while (i + 2) < n:
    
    if arr[i] + arr[i + 1] > arr[i + 2] and arr[i] + arr[i + 2] > arr[i + 1] and arr[i + 2] + arr[i + 1] > arr[i]:
        
        print(arr[i + 2],arr[i + 1],arr[i])
        
        break
        
    i += 1
    
if i + 2 >= n:
    
    print("-1")
