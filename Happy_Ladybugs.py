for _ in range(int(input())):
    
    n = int(input())
    
    b = input()
    
    d = dict()
    
    flag = 0
        
    for i in b:
            
        if i != '_':
            
            d[i] = 0
            
    for i in b:
            
        if i != '_':
            
            d[i] += 1
                
    for i in d.keys():
        
        if d[i] == 1:
            
            flag = 1
            
            break
            
    if flag == 1:
        
        print("NO")
        
    else:
        
        if b.count('_') == 0:

            flag = 0

            for i in range(1,len(b)-1):

                if b[i] == b[i-1]:

                    continue

                if b[i] == b[i+1]:

                    continue

                flag = 1

                break

            if flag == 0:

                print("YES")

            else:

                print("NO")
                
        else:
            
            print("YES")
