class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        x,d,c = set(),dict(),0
        
        for i in arr:
            
            if i in d:
                
                d[i] += 1
                
            else:
                
                d[i] = 1
                
        for i in d:
            
            if 2*i == k and i not in x:
                
                x.add(i)
                
                c += (d[i]*(d[i]-1))//2
            
            elif (k-i in d and i not in x and k-i not in x):
                
                c += d[i]*d[k-i]
                
                x.add(i)
                x.add(k-i)
            
        return c
