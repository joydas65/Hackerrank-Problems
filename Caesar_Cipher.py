n = int(input())

s = input()

k = int(input())

ans = ""

k = k % 26

for i in s:
    
    if ord(i) >= 65 and ord(i) <= 90:
        
        if ord(i) + k > 90:
            
            ans += chr(ord(i) + k - 26)
            
        else:
            
            ans += chr(ord(i) + k)
            
    elif ord(i) >= 97 and ord(i) <= 122:
        
        if ord(i) + k > 122:
            
            ans += chr(ord(i) + k - 26)
            
        else:
            
            ans += chr(ord(i) + k)
            
    else:
        
        ans += i
            
print(ans)
