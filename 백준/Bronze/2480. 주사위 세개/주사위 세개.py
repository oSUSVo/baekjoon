A, B, C = map(int, input().split(" "))
price = 0

if A == B and B == C:
    price = 10000 + A * 1000
elif A == B:
    price = 1000 + A * 100
elif B == C:
    price = 1000 + B * 100
elif C == A:
    price = 1000 + C * 100
else:
    price = 100 * max(A,B,C)
print(price)