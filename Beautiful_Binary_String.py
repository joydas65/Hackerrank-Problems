n = int(input())

s = input()

n,ind,ans = len(s),0,0

while ind < n:

    if ind+3 <= n and s[ind:ind+3] == '010':

        ans += 1

        ind += 3

    else:

        ind += 1

print(ans)
