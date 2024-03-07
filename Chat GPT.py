def staircase(n):
    for i in range(1, n+1):
        spaces = n - i
        print(" " * spaces + "#" * i)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

