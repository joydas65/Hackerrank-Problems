for _ in range(int(input())):
    
    m = int(input())
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    s = set()
    
    d = dict()
    
    for i in range(n):
        
        if (m - arr[i]) in s:
            
            break
            
        else:
            
            s.add(arr[i])
            
        d[arr[i]] = i
        
    print(d[m-arr[i]] + 1,i+1)
