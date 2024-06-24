def fibs():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def roots(x):
    y = x
    while 1:
        yield y
        y = 0.5 * (y + x / y)

def primes():
    p = 2
    found_prime = False
    while 1: 
        yield p
        found_prime = False
        while (not found_prime):
            p += 1
            for i in range(2, p):
                if p % i == 0:
                    break
                if i == p - 1:
                    found_prime = True

def hammings():
    h = 1
    p = primes()
    p_list = [next(p)]
    while 1:
        yield h
        found_hamming = False
        while (not found_hamming):
            h += 1
            # h div list
            div_list = []
            p_div_list = []
            # add prime to list until last prime >= h
            while (p_list[len(p_list) - 1] < h):
                p_list.append(next(p))
            # calculate div list for h
            for i in range(2, h + 1):
                if (h % i == 0):
                    div_list.append(i)
            found_wrong_div = False
            for div in div_list:
                if div in p_list:
                    if (div != 2 and div != 3 and div != 5):
                        found_wrong_div = True
            if (not found_wrong_div):
                found_hamming = True
            

if __name__ == "__main__":
    g1 = fibs()
    g2 = roots(4)
    g3 = primes()
    g4 = hammings()
    print([next(g1) for i in range(10)])
    print([next(g2) for i in range(10)])
    print([next(g3) for i in range(20)])
    print([next(g4) for i in range(20)])
