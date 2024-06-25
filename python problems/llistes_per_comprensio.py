def my_map(f, L):
    return ([f(item) for item in L])

def my_filter(f, L):
    return ([item for item in L if f(item) == True])

def factors(n):
    return ([i for i in range(1, n + 1) if n % i == 0])

def triplets(n):
    return ([(a, b, c) for a in range(1, n + 1) for b in range(1, n + 1) for c in range(1, n + 1) if a * a + b * b == c * c])

if __name__ == "__main__":
    print(my_map(lambda x: x + 1, [1, 2, 3, 4]))
    print(my_filter(lambda x: x > 3, [1, 2, 3, 4]))
    print(factors(10))
    print(triplets(20))