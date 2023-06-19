def min_cost_to_top(n, costs):
    dp = [0] * n

    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

    return dp[-1]


n = int(input())
costs = list(map(int, input().split()))

result = min_cost_to_top(n, costs)
print(result)
