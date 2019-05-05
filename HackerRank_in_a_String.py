for _ in range(int(input())):

    s = input()

    word = "hackerrank"

    ind1,ind2 = 0,0

    while ind2 < len(s):

        if word[ind1] == s[ind2]:

            ind1 += 1

            if ind1 == 10:

                break

        ind2 += 1

    if ind1 == 10:

        print("YES")

    else:

        print("NO")
