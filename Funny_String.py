for _ in range(int(input())):

    s = input()

    n,flag = len(s),0

    for i,j in enumerate(s):

        if i < n-1:

            v1 = abs(ord(s[i])-ord(s[i+1]))

        if n-i-1 >= 1:

            v2 = abs(ord(s[n-i-1])-ord(s[n-i-2]))

        if v1 != v2:

            flag = 1

            break

    if flag == 0:

        print("Funny")

    else:

        print("Not Funny")
