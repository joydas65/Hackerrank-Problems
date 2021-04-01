n = int(input())

d = dict()

for i in range(n):
    
    name,m1,m2,m3 = map(str, input().split())
    
    d[name] = [float(m1),float(m2),float(m3)]
    
query = input()

s = str(sum(d[query])/3)

point = s.index('.')

if len(s[point+1:]) == 1:
    
    s += "0"
    
else:
    
    s = s[:point] + s[point:point+3]
    
print(s)
