t1,t2,n = map(int, input().split())

ti = t1

t_iplus1 = t2

temp = 0

for _ in range(n-2):
    
    t_iplus2 = ti + (t_iplus1 * t_iplus1)
    
    temp = t_iplus1
    
    t_iplus1 = t_iplus2
    
    ti = temp
    
print(t_iplus2)
