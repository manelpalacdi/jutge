# Write a program that, given n different words s1, …, sn, 
# prints all the subsets that can be made up with the words.

from itertools import chain, combinations

def powerset(n, s):
    for i in range(1 << n):
        print(list(s[j] for j in range(n) if (i & (1 << j))))


if __name__ == "__main__":
    n = int(input())
    words = input()
    powerset(n, words.split(" "))