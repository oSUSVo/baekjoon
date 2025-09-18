N = int(input())

for i in range(N):
    A, B = map(int, input().split(" "))
    C = A + B
    x = f"#{i + 1}:"
    print("Case", x, f"{A} + {B} =", C)