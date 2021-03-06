
'''
Find minimum set of odd numbers to satisfy Solaz conjecture:
every even integer greater than two is the sum of two odd numbers from the minimum set.

Implementation use: combinations function from itertools
This method takes a list and return a list of tuples with all possible combination of length r

'''

import numpy as np
from scipy.special import comb
from itertools import combinations
import time
from tqdm import tqdm

'''
find minimum set of odd numbers to satisfy:
every even integer smaller then N is the sum of two odd numbers from the minimum set.
'''
# find at list one pair in the pair list satisfy p0 + p1 == n .
# return not found
def find_pair(paires,n):
    for pair in paires:  # check identical paires
        if n == pair[0] + pair[1]:
            return pair
    return None


def get_all_paires(curr_set):
    mixed_paires = combinations(curr_set, 2)
    # need to add identical paires ( 3,3   5,5 , 9,9...etc)
    identical_paires = [(x, x) for x in curr_set]
    return identical_paires + list(mixed_paires)

# check if current set is satisfy Solaz conjecture for all even integers < N :
def sufficient(curr_set,N):
    all_paires = get_all_paires(curr_set)
    for n in range(2,N+2,2):
        if find_pair(all_paires,n) == None:
            return False
    return True


def find_minimum_set(N):

    print(f'find minimum odd set for {N}')
    all_odds = range(1,N,2)
    # all possible combination of length r in a list form.
    for r in range(2,N):
        rsets_count_= comb(len(range(1,N,2)),r,exact=True, repetition=True)
        print(f'check {rsets_count_} odd sets with {r} odd numbers')
        all_rsets = combinations(all_odds, r)
        for rset in tqdm(all_rsets,total=rsets_count_):
            if sufficient(rset,N):
                return rset,r

    return None,None


import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(f'usage python {sys.argv[0]} <N>')
        exit(1)

    N = np.int(sys.argv[1])
    start = time.perf_counter()
    min_set,minset_len = find_minimum_set(N)
    end = time.perf_counter()
    if min_set is None:
        print(end - start)
        print ('minimum set not found goldbach was wrong')
        exit(0)

    all_evens = range(2,N+2,2)
    for n in all_evens:
        pair = find_pair(get_all_paires(min_set), n)
        print(f'{n}={pair[0]}+{pair[1]}')

    print(f'{int(1000 * (end - start))} milisec- minimum set length: {minset_len} \n {list(min_set)} ')

