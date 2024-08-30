import math
import time

def sieve():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # list for now
    # will be replaced by sieve of Eratosthenes
    # then sieve of Atkin

# binary search function not tested yet in vscode
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mean = (left + right) // 2 # floor
        if array[mean] == target:
            return True
        elif array[mean] < target:
            mean = left + 1
        else:
            mean = right - 1
    return False

def is_prime(n):
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    if n < 49:
        return True
    if (n %  7) == 0 or (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0 or \
       (n % 19) == 0 or (n % 23) == 0 or (n % 29) == 0 or (n % 31) == 0 or \
       (n % 37) == 0 or (n % 41) == 0 or (n % 43) == 0 or (n % 47) == 0:
        return False
    if n < 2809:
        return True
    if n < 65077:
        return pow(2, n / 2, n) in [1, n - 1] and n not in [8321, 31621, 42799, 49141, 49981]

    searchLimit = 2**32 - 1

def main():
    while 1:
        print('------------------------------------------')
        print('|         Xterminal1 : PrimeTest         |')
        print('------------------------------------------')
        print()

        try:
            n = int(input('Integer: '))
        except ValueError:
            print('Invalid input. Enter an integer.')
        
        print(f'Integer: prime\n') if is_prime(n) else print(f'Integer: nonprime\n')

if __name__ == "__main__":
    main()
