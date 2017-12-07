import sys
from collections import Counter

divisor = 10**9 + 7

ltk_memo = {}
def fill_ltk(l):
    ltk_memo[1] = {i:1 for i in range(10)}
    for i in range(2, l+1):
        ltk_memo[i] = Counter()
        for num, cnt in ltk_memo[i-1].items():
            for digit in range(10):
                ltk_memo[i][num+digit] += cnt
fill_ltk(250)

def length_to_k(l,k):
    return ltk_memo[l].get(k, 0)

memo = {}
# Number of non-negative integers less than or equal to 'n' that sum to 'k'
# @profile
def sum_to_k(n, k):
   # memoization
    if (n,k) in memo:
        return memo[(n,k)]
    m = len(n)
    if m == 1:
        if k < 0 or k >=10:
            return 0
        else:
            return 1 if k<=int(n) else 0
    a1 = int(n[0])
    total = 0
    for digit in range(a1):
        total += length_to_k(m-1, k-digit)
    total += sum_to_k(n[1:], k-a1)
    memo[(n,k)] = total % divisor
    return total % divisor


pair_memo = {}
# @profile
def countPairs(n):
    m = len(n)
    if m==1:
        lst = [0,1,3,6,10,15,21,28,36,45]
        return lst[int(n[0])]
    if n in pair_memo:
        return pair_memo[n]
    if n[0] == "0":
        pair_memo[n] = countPairs(n[1:])
        return pair_memo[n]
    else:
        total = 0
        # Extract first digit and count
        first_digit = int(n[0])
        # Fix two number's first digit as same number and calculate all pairs
        total += first_digit * countPairs('9'*(m-1))
        total = total % divisor
        # Set first two digits as different number and calculate all pairs
        for diff in range(1, first_digit):
            left = 0
            for j in range(diff-1):
                #left += sum_to_k('9'*(m-1), j)
                left += length_to_k(m-1, j)
            for sod in range(9*(m-1)+1):
                left += length_to_k(m-1, sod+diff-1) # number of nn-integers that sum to less than or equal to 'sod'
                right = length_to_k(m-1, sod)
                total += (first_digit-diff) * (left*right)
        total = total % divisor
        # Fix second number's first_digit as "first_digit" and find all combinations
        for i in range(first_digit):
            diff = first_digit - i
            left = 0
            for j in range(diff-1):
                left += length_to_k(m-1, j)
            for sod in range(9*(m-1)+1):
                left += length_to_k(m-1, sod+diff-1) # number of nn-integers that sum to a number that is less than or equal to 'sod'
                right = sum_to_k(n[1:], sod)
                total += left*right
        total = total % divisor
        total += countPairs(n[1:])
        total = total % divisor
        pair_memo[n] = total
        return total


if __name__ == "__main__":
    n = input().strip()
    result = countPairs(n)
    print(result)
