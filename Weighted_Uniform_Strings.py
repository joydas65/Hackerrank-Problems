s = input()

n = int(input())

lomba_list,l,c,x = [],len(s),1,set()

for i in range(1,l):
    
    if s[i] == s[i-1]:
        
        c += 1
        
    else:
        
        lomba_list.append((s[i-1],c))
        
        c = 1
        
lomba_list.append((s[-1],c))

for i in lomba_list:
    
    v = ord(i[0])-96
    
    for j in range(1,i[1]+1):
        
        x.add(v*j)
        
for i in range(n):
    
    query = int(input())
    
    if query in x:
        
        print("Yes")
        
    else:
        
        print("No")
