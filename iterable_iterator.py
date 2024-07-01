import itertools
from math import comb
def probability_of_a(N, letters, K):
    # Count the number of 'a' in the list
    count_a = letters.count('a')
    count_not_a = N - count_a

    if count_not_a < K:
        # If there are not enough non-'a' letters to pick K indices, the probability is 1
        return 1.0

    # Calculate the total ways to choose K indices from N
    total_ways = comb(N, K)

    # Calculate the ways to choose K indices from non-'a' letters
    non_a_ways = comb(count_not_a, K)

    # Calculate the probability of picking at least one 'a'
    prob_no_a = non_a_ways / total_ways
    prob_at_least_one_a = 1 - prob_no_a

    return round(prob_at_least_one_a, 4)


# Example usage
N = 4
letters = ['a', 'a', 'c', 'd']
K = 2
print(probability_of_a(N, letters, K))  # Output: 0.8333


def calc_prob(arr,k):
    n = len(arr)
    indices = range(n)
    tot_comb = list(itertools.combinations(indices, k))
    count_with_a = 0
    for com in tot_comb:
        if any(arr[i] == "a" for i in com):
            count_with_a += 1
    prob = count_with_a / len(tot_comb)
    return prob

arr = ['a', 'a', 'c', 'd']
print(f"{calc_prob(arr, 2)}")
