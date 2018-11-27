from collections import Counter

queries = []

for _ in range(int(input())):
    
    queries.append(list(map(int, input().split())))

f = Counter()

d = Counter()

answer = []

for i in queries:
    
    if i[0] == 1:
        
        d[f[i[1]]] -= 1
        
        f[i[1]] += 1
        
        d[f[i[1]]] += 1

    elif i[0] == 2:
        
        if f[i[1]] > 0:
            
            d[f[i[1]]] -= 1
            
            f[i[1]] -= 1
            
            d[f[i[1]]] += 1

    elif i[0] == 3:
        
        if d[i[1]]>0:
            
            answer.append(1)
            
        else:
            
            answer.append(0)
            
for i in answer:
    
    print(i)
