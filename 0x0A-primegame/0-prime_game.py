#!/usr/bin/python3
"""
Solve The Prime Game
"""


def isWinner(x, nums):
    """Determines the winner of the Prime Game after x rounds."""
    def sieve(n):
        """Generate a list of primes up to n using Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    if not nums or x < 1:
        return None

    # Precompute primes up to the largest n in nums
    max_n = max(nums)
    primes_up_to_n = sieve(max_n)

    # Store the number of primes up to any index i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes_up_to_n else 0)

    # Simulate each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_left = prime_count[n]
        if primes_left % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
