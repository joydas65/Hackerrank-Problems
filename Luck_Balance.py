n,k = map(int, input().split())

im = []

unim = []

for i in range(n):
    
    li,ti = map(int, input().split())
    
    if ti == 1:
        
        im.append(li)
        
    else:
        
        unim.append(li)
        
im = sorted(im,reverse = True)

print(sum(im[:k])+sum(unim)-sum(im[k:]))
