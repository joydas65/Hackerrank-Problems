n = int(input())

arr = list(map(int, input().split()))

x = arr.copy()

arr = sorted(arr)

if arr == x:
    
    print("yes")

else:
    
    d1 = dict()

    d2 = dict()

    for i in range(n):

        d2[arr[i]] = i

    for i in range(n):

        d1[x[i]] = i

    for i in range(n):

        if arr[i] != x[i]:

            break

    actual_index = d2[arr[i]]

    array_index = d1[arr[i]]

    x[actual_index],x[array_index] = x[array_index],x[actual_index]

    c = 0

    flag1 = 0

    flag2 = 0

    if x == arr:

        c += 1
        
        flag1 = 1

    x[actual_index],x[array_index] = x[array_index],x[actual_index]

    x = x[:actual_index] + x[actual_index:array_index + 1][::-1] + x[array_index + 1:]

    if x == arr:

        c += 1
        
        flag2 = 1

    if c == 2:
        
        print("yes")

        print("swap",end = " ")
        
        print(actual_index + 1,array_index + 1)
        
    elif c == 1 and flag1 == 1:
        
        print("yes")
        
        print("swap",end = " ")
        
        print(actual_index + 1,array_index + 1)
        
    elif c == 1 and flag2 == 1:
        
        print("yes")
        
        print("reverse",end = " ")
        
        print(actual_index + 1,array_index + 1)
        
    else:
        
        print("no")

