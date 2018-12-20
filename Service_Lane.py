n,t = map(int, input().split())

arr = list(map(int, input().split()))

d = dict()

d[1] = []

d[2] = []

d[3] = []

for i in range(n):
    
    d[arr[i]].append(i)
    
flag = 0
    
for _ in range(t):
    
    entry,exit = map(int, input().split())
    
    for i in d[1]:
        
        if i >= entry and i <= exit:
            
            flag = 1
            
            break
            
        else:
            
            if i > exit:
                
                break
                
    if flag == 1:
        
        print("1")
        
    else:
        
        for i in d[2]:
            
            if i >= entry and i <= exit:
                
                flag = 1
                
                break
                
            else:
                
                if i > exit:
                    
                    break
                    
        if flag == 1:
            
            print("2")
            
        else:
            
            print("3")
            
    flag = 0
                        
                
