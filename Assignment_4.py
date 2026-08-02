# Memoization approach (Top-Down): Computes recursively and stores results in a dictionary
def fibonacci_memo(n, memo={}):
    # Return the cached result if it has already been computed
    if n in memo:
        return memo[n]

    # Base cases: fib(0) = 0 and fib(1) = 1
    if n <= 1:
        return n

    # Compute recursively, store the result in the memo dictionary, and return it
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation approach (Bottom-Up): Iteratively builds up solutions in an array
def fibonacci_tab(n):
    # Base cases for n = 0 or n = 1
    if n <= 1:
        return n

    # Initialize a DP table to store Fibonacci numbers up to n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Fill the table iteratively from index 2 to n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return the nth Fibonacci number
    return dp[n]


# Main execution block
n = int(input("Enter n: "))

# Print results from both dynamic programming techniques
print("Memoization:", fibonacci_memo(n))
print("Tabulation:", fibonacci_tab(n))