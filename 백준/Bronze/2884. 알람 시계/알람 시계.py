A, B = map(int, input().split(" "))

B -= 45

if B >= 0:
    print(f"{A} {B}")
elif B < 0:
    A -= 1
    B += 60
    if A >= 0:
        print(f"{A} {B}")
    elif A < 0:
        A += 24
        print(f"{A} {B}")