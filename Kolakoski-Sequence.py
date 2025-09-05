n = int(input("Enter number of iterations: "))

x = y = -1

for i in range(n):
    x = x // 2 ^ y
    y <<= x % 2
    print(x % 2 + 1, end=" ")
