s = input()

d,n = dict(),len(set(s))

for i in s:

    if i not in d:

        d[i] = 1

    else:

        d[i] += 1

freqs = list()

for i in d:

    freqs.append(d[i])

freqs = sorted(freqs)

val = freqs[0]

if val*n == sum(freqs):

    print("YES")

else:

    if val == freqs[-2] and (freqs[-1] - val == 1):

        print("YES")

    else:

        if freqs[-1] == freqs[1] and freqs[0] == 1:

            print("YES")

        else:

            print("NO")
