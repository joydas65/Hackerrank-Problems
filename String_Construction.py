for _ in range(int(input())):

    s = input()

    x,ans = set(),0

    for i in s:

        if i not in x:

            ans += 1

            x.add(i)

    print(ans)
