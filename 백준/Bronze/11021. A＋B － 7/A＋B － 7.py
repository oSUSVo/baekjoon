N = int(input())

for i in range(N):
    A, B = map(int, input().split(" "))
    x = f"#{i + 1}:"
    print("Case", x, A + B)