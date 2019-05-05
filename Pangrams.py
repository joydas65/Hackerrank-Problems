s = input()

d,flag = dict(),0

for i in "abcdefghijklmnopqrstuvwxyz":

    d[i] = False

d[' '] = False

s = s.lower()

for i in s:

    d[i] = True

for i in "abcdefghijklmnopqrstuvwxyz":

    if d[i] == False:

        flag = 1

        break

if flag == 1:

    print("not pangram")

else:

    print("pangram")
