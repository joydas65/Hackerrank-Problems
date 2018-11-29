p = int(input())

q = int(input())

i = p

ans = []

while i <= q:
    
    d = len(str(i))
    
    x = str(i ** 2)
    
    n = len(x)
    
    if n - d == 0:
    
        if i == int(x[n - d:]):

            ans.append(i)
    
    else:
        
        if i == int(x[:n - d]) + int(x[n - d:]):

            ans.append(i)
        
    i += 1
    
if ans == []:
    
    print("INVALID RANGE")
    
else:
    
    for i in ans:
        
        print(i,end = " ")
