""" GoldBach Conjecture representation refactored in python for better efficiency with dependencies and Libraries
    Refactored: 3/04/2024
    Author: Layden E. Halcomb

"""

import matplotlib.pyplot as plt


def sum_separation(num):
    check = False  # Boolean for checking if the number is even.
    counter = 0
    for i in range(2, num // 2 + 1):  # For loop that begins the process of separating the even number into sum of two primes.
        if check_prime(i):  # If the number is prime it runs down to the function below
            if check_prime(num - i):
                # print(num, "=", i, "+", num - i)
                check = True
                counter += 1

    """ if not check:
        print(num, "cannot be represented as the sum of two prime numbers.")
    print("The number of equations for", num, "is", counter) """
    return counter

def check_prime(n):  # Function created to check if number is prime and returns that number via driver code for loop.
    is_prime = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def update_prime_intensity_map(num, prime_intensity_map):
    for i in range(2, num // 2 + 1):
        if check_prime(i) and check_prime(num - i):
            prime_intensity_map[i] = prime_intensity_map.get(i, 0) + 1 #adds to the value from the first prime in the sum and its corresponding frequency
            prime_intensity_map[num - i] = prime_intensity_map.get(num - i, 0) + 1 #adds to the value from the second prime in the sum and its corresponding frequency


if __name__ == "__main__":
    assert check_prime(5) == True
    n = 20000
    #sum_separation(n)

    #print("Printing", n, "amount of equations")
    even_number_eq = {}
    prime_intensity_map = {}

    eq_count_list = []

    for i in range(2, n + 1):
        num = 2 * i  # Generating even numbers
        equation_count = sum_separation(num)
        even_number_eq[num] = equation_count
        update_prime_intensity_map(num, prime_intensity_map)
        #print()  # Add a newline for better readability

    """ # Print the map
    print("Even numbers and their corresponding equations count:")
    for even_number, equations_count in even_number_eq.items():
        print("Even number:", even_number, ", Equations count:", equations_count)
        eq_count_list.append(equations_count) """

    # Print Prime Intensity Analysis
    
    for prime_number, intensity in prime_intensity_map.items():
        if check_prime(prime_number):
            print("Prime number:", prime_number, ", Intensity:", intensity) 
    

    # Plotting prime frequencies
    """  
    plt.hist(eq_count_list, bins=range(min(eq_count_list), max(eq_count_list) + 1), alpha=0.75)
    plt.xlabel('Equations Count')
    plt.ylabel('Frequency')
    plt.title('Prime Frequencies')
    plt.grid(True)
    plt.show() 
    """
    # Plotting Equations count
    # plt.figure(figsize=(8, 6))
    # plt.scatter(range(2, n + 1), eq_count_list, marker='o')
    # plt.xlabel('Even Numbers')
    # plt.ylabel('Equations Count')
    # plt.title('Equations Count for Even Numbers')
    # plt.grid(True)
    # plt.show()
    
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