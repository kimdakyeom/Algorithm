import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        # num의 제곱근까지만 검사해도 됨
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if isPrime(i):
        sys.stdout.write(str(i) + '\n')