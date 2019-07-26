n = int(input())

arr = list(map(int, input().split()))

dp = [arr[0],max(arr[1],arr[0])]

max_seen_so_far = max(arr[0],arr[1])

for i in range(2,n):

    dp.append(max(arr[i],arr[i]+dp[i-2],max_seen_so_far))

    max_seen_so_far = max(max_seen_so_far, dp[i])

print(max(dp))
