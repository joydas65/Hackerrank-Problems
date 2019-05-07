import sys

h = sys.maxsize

for _ in range(int(input())):
    
    s = input()
    
    if len(s) == 1:
        
        print("NO")
        
    elif s[0] == '0':
        
        print("NO")
        
    else:
    
        num,n,prev,ans,t = 1,len(s),0,sys.maxsize,1

        while num <= n//2:
                    
            flag,t,prev,ans = 0,num,0,sys.maxsize
                    
            while num+prev+t <= n:
                        
                v1 = int(s[prev:prev+t])
                
                v2 = s[prev+t:num+prev+t]
                        
                if v2[0] != '0' and int(v2)-v1 == 1:
                            
                    prev += t
                            
                    ans = min(ans, v1)
                            
                    t = num
                    flag = 0
                            
                else:
                    
                    flag = 1
                            
                    num += 1
                            
                    if abs(num-t) > 1:
                                
                        num -= 1
                                
                        prev,t = 0,num
                                
                        flag = 1
                                
                        break
                        
            #print(prev,num,t)
                        
            if prev+t < n:
                
                v1 = int(s[prev:prev+t])
                
                v2 = s[prev+t:]
                
                if v2[0] != '0' and int(v2)-v1 == 1:
                    
                    ans = min(ans, v1)
                    
                    flag = 0
                    
                else:
                    
                    if num+prev+t >= n:
                    
                        flag = 1

                        break
                                
            if h != ans and flag == 0:
                        
                print("YES",ans)
                        
                break
                        
        if (h == ans and flag == 0) or flag == 1:
            
            print("NO")
