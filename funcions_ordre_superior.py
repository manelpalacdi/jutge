from functools import reduce

def evens_product(L):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, L), 1)

def reverse(L):
    n = len(L)
    return ([reduce(lambda x, y: y, L[:n-i]) for i in range(len(L))])

def zip_with(f, L1, L2):
    return(list(map(lambda x: f(x[0], x[1]), zip(L1, L2))))

def count_if(f, L):
    return(len(list(filter(f, L))))

if __name__ == "__main__":
    print(evens_product([1, 2, 3, 4]))
    print(reverse([1, 2, 3, 4]))
    print(reverse([1, 2, 3, 4]))
    print(zip_with(lambda x, y: x * y, [1, 2, 3], [10, 2]))
    print(count_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))