import sys

n = int(sys.stdin.readline())  # 몇 줄 받을지 먼저 입력
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
