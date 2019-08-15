for _ in range(int(input())):

    s = list(input())

    n = len(s)

    i = n - 1

    while i >= 1 and ord(s[i-1]) >= ord(s[i]):

        i -= 1

    if i == 0:

        print("no answer")

    else:

        j = n - 1

        #print(i)

        while ord(s[i-1]) >= ord(s[j]):

            j -= 1

        s[i-1],s[j] = s[j],s[i-1]

        j = n - 1

        while i < j:

            s[i],s[j] = s[j],s[i]

            i += 1

            j -= 1

        for i in s:

            print(i,end="")

        print()

        

