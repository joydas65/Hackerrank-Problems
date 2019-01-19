for _ in range(int(input())):
    
    n = int(input())
    
    s = ""
    
    while n != 0:
        
        if n % 2 == 0:
            
            s = '0' + s
            
        else:
            
            s = '1' + s
            
        n //= 2
        
    for i in range(32 - len(s)):
        
        s = '0' + s
        
    print(s)
            
    ans = ""
    
    for i in s:
        
        if i == '1':
            
            ans += "0"
            
        else:
            
            ans += "1"
            
    final_answer = 0
    
    p = 31
    
    for i in range(32):
        
        if ans[i] == "1":
        
            final_answer += (2 ** p)
        
        p -= 1
        
    print(final_answer)
