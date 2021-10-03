import sys

def is_prime(num):
    try:
        num = int(num)
    except:
        return False

    if num < 1:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in sys.argv[1:]:
        if is_prime(i):
            print(i)
