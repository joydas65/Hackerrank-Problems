x = 0

s = input()

t = input()

k = int(input())

m = len(s)

n = len(t)

for i in range(min(m,n)):
    
    if s[i] == t[i]:
        
        x += 1
        
    else:
        
        break
        
if (m + n - (2 * x)) > k:
    
    print("No")
    
elif (m + n - (2 * x)) % 2 == (k % 2):
    
    print("Yes")
    
elif m + n - k < 0:
    
    print("Yes")
    
else:
    
    print("No")
