n = int(input())

arr = [[str(j) for j in input()] for i in range(n)]

flag = 0

for i in range(n):
    
    for j in arr[i]:
        
        if j == ' ':
            
            flag = 1
            
            arr[i].remove(j)
            
grid = []

row = 0
            
for i in range(n):
    
    grid.append([])
    
    if i == 0 or i == n - 1:
        
        for j in range(n):
            
            grid[row].append(arr[i][j])
            
        row += 1
        
    else:
            
        for j in range(n):

            if j == 0 or j == n - 1:

                grid[row].append(arr[i][j])

            elif int(arr[i][j]) > int(arr[i+1][j]) and int(arr[i][j]) > int(arr[i-1][j]) and int(arr[i][j]) > int(arr[i][j+1]) and int(arr[i][j]) > int(arr[i][j-1]):

                grid[row].append('X')

            else:

                grid[row].append(arr[i][j])

        row += 1
            
if flag == 0:

    for i in range(n):

        for j in range(n):

            print(grid[i][j],end = "")

        print()
        
else:
    
    for i in range(n):

        for j in range(n):

            print(grid[i][j],end = " ")

        print()
