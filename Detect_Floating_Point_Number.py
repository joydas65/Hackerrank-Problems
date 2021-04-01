for _ in range(int(input())):
    
    s = input()
    
    try:
        
        x = float(s)
        
        if '.' not in s:
            
            print("False")
            
        else:
        
            print("True")
        
    except ValueError:
        
        print("False")
