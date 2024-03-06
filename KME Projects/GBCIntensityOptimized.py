import matplotlib.pyplot  as plt
import math

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(limit + 1) if primes[i]]


# Use this primes_list for checking primes
def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for prime in primes_list:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

# Modify sum_separation function to use primes_list
def sum_separation(num):
    counter = 0
    for prime in primes_list:
        if prime > num // 2:
            break
        if check_prime(num - prime):
            counter += 1
    return counter

def update_prime_intensity_map(num, prime_intensity_map):
    for i in range(2, num // 2 + 1):
        if check_prime(i) and check_prime(num - i):
            prime_intensity_map[i] = prime_intensity_map.get(i, 0) + 1 #adds to the value from the first prime in the sum and its corresponding frequency
            prime_intensity_map[num - i] = prime_intensity_map.get(num - i, 0) + 1 #adds to the value from the second prime in the sum and its corresponding frequency

if __name__ == "__main__":

    # Generate a list of primes up to a certain limit
    primes_list = sieve_of_eratosthenes(100000)

    n = 20000
    even_number_eq = {}
    prime_intensity_map = {}
    for i in range(1, n // 2 + 1):
        num = 2 * i
        equation_count = sum_separation(num)
        even_number_eq[num] = equation_count
        update_prime_intensity_map(num, prime_intensity_map)

     #Plotting Prime Intensity
    prime_numbers = list(prime_intensity_map.keys())
    intensity_values = list(prime_intensity_map.values())
    plt.figure(figsize=(8, 6))
    #plt.plot(prime_numbers, intensity_values, marker='o', linestyle='-')
    plt.scatter(prime_numbers, intensity_values)
    plt.xlabel('Prime Numbers')
    plt.ylabel('Intensity')
    plt.title('Prime Number Intensity')
    plt.grid(True)
    # for x, y in zip(prime_numbers, intensity_values):
    #     plt.text(x, y, f'({x}, {y})', fontsize=8, ha='right')

    
    plt.show()

