n,k = map(int, input().split())

arr = list(map(int, input().split()))

ones = []

for i,j in enumerate(arr):
    
    if j == 1:
        
        ones.append(i)
        
ans = 0

start = k-1

x = len(ones)

install = set()

range_covered = 0

while True:
    
    flag = 0
    
    left,right = 0,x-1
    
    while left <= right:
        
        mid = (left+right)//2
        
        if ones[mid] > start:
            
            right = mid - 1
            
        elif ones[mid] < start:
            
            left = mid + 1
            
        else:
            
            if start < n and start not in install:
            
                install.add(start)

            else:

                break
            
            ans += 1
            
            start += k
            
            range_covered = start
            
            start += (k-1)

            #print(ans,left,right,start)
            
            if start >= n:
                
                start = n-1
            
            flag = 1
            
            break

        #print(left,right)
            
    if flag == 0:

        #print(ans,left,right,start)
        
        if right >= 0 and ones[right]+k-1 >= start and ones[right] not in install:
            
            ans += 1
            
            start = (ones[right] + k)
            
            range_covered = start
            
            start += (k-1)
            
            if start >= n:
                
                start = n - 1
            
            install.add(ones[right])
            
        else:

            ans += 1

            start = (ones[right]+k)

            range_covered = start

            start += (k-1)

            if start >= n:

                start = n - 1

            if ones[right] not in install:

                install.add(ones[right])

            else:
            
                break

        #print(ans,left,right,start)
            
if range_covered >= n:
    
    print(ans-1)
    
else:
    
    print("-1")

#print(ones)

#print(range_covered)
