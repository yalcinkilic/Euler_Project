import pyprimes as py

def compute_Pnk(n,len,prime_list):
    if n<2 :
        return 0

    if len == 1 and n % 2 == 0 :
        return 1

    if len == 1 and n % 2 == 1:
        return 0

    if n == prime_list[len-1]:
        return 1 + compute_Pnk(n,len-1,prime_list)

    if n < prime_list[len-1]:
        return compute_Pnk(n,len-1,prime_list)

    return compute_Pnk(n-prime_list[len-1],len,prime_list) + compute_Pnk(n,len-1,prime_list)
def compute_P(n):
    prime_list = list(py.primes_below(n))
    return compute_Pnk(n,len(prime_list),prime_list)

num = 10
while compute_P(num) < 5000:
    num += 1

print(num)
