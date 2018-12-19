numbers = "0123456789"

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

special_characters = "!@#$%^&*()-+"

n = int(input())

s = input()

flag1 = 0

flag2 = 0

flag3 = 0

flag4 = 0

ans = 0

for i in s:
    
    if i in numbers:
        
        flag1 = 1
        
    elif i in lower_case:
        
        flag2 = 1
        
    elif i in upper_case:
        
        flag3 = 1
        
    elif i in special_characters:
        
        flag4 = 1
        
if flag1 == 0:
    
    ans += 1
    
if flag2 == 0:
    
    ans += 1
    
if flag3 == 0:
    
    ans += 1
    
if flag4 == 0:
    
    ans += 1
    
n += ans

if n < 6:
    
    ans += (6 - n)
    
print(ans)
