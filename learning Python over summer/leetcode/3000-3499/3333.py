def count_possible_original_strings(word: str, k: int) -> int:
    MOD = 10**9 + 7

    # Step 1: Identify consecutive character runs
    runs = []
    n = len(word)
    i = 0
    while i < n:
        j = i
        while j < n and word[j] == word[i]:
            j += 1
        runs.append(j - i)
        i = j

    m = len(runs)
    # Step 2: Calculate the total number of assignments
    total = 1
    for c in runs:
        total = (total * c) % MOD

    # Step 3: Determine if all assignments satisfy the sum constraint
    if m > k - 1:
        return total

    sum_c = sum(runs)
    if sum_c < k:
        return 0

    # Step 4: Dynamic Programming to count assignments with sum <= k-1
    dp = [0] * k
    dp[0] = 1  # Base case: no runs assigned yet

    for c_j in runs:
        # Compute prefix sums for current DP state
        prefix = [0] * k
        prefix[0] = dp[0]
        for s in range(1, k):
            prefix[s] = (prefix[s - 1] + dp[s]) % MOD

        # Update DP for the next run
        dp_new = [0] * k
        for s in range(1, k):
            t_max = min(c_j, s)
            if s - t_max - 1 >= 0:
                dp_new[s] = (prefix[s - 1] - prefix[s - t_max - 1]) % MOD
            else:
                dp_new[s] = prefix[s - 1] % MOD
        dp = dp_new

    # Step 5: Sum the valid assignments where the total sum is <= k-1
    sum_assignments = 0
    for s in range(m, min(k, sum_c + 1)):
        sum_assignments = (sum_assignments + dp[s]) % MOD

    # Step 6: Calculate the final answer
    answer = (total - sum_assignments) % MOD
    return answer