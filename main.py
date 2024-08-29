import math
import time

def sieve():
    pass

# binary search function not tested yet in vscode
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mean = (left + right) // 2 # floor
        if mean == target:
            return True
        elif mean > target:
            mean = right - 1
        else:
            mean = left + 1
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
