import math

def myFunc(rows,cols,t,p):
    
    print(rows,cols)
    
    k = 1
    
    while k <= cols:
        
        v = k - 1
        
        while v < p:
            
            print(t[v],end = "")
            
            v += cols
            
        print(" ",end = "")
        
        k += 1

s = input()

x = ""

for i in s:
    
    if i != ' ':
        
        x += i
        
l = len(x)

square_root = math.sqrt(l)

lb = math.floor(square_root)

ub = math.ceil(square_root)

print(lb,ub)

if lb*(ub - 1) >= l:
    
    myFunc(lb,ub-1,x,l)
    
elif lb * ub >= l:
    
    myFunc(lb,ub,x,l)
    
elif (lb + 1) * ub >= l:
    
    myFunc(lb + 1,ub,x,l)
