for _ in range(int(input())):
    
    b,w = map(int, input().split())
    
    bc,wc,z = map(int, input().split())
    
    a1 = (b * bc) + (w * wc)
    
    a2 = ((b + w) * bc) + (w * z)
    
    a3 = ((b + w) * wc) + (b * z)
    
    print(min(a1,a2,a3))
