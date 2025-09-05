A, B = map(int, input().split(" "))
C = int(input())

finish_hr = A + ((C + B) // 60)
finish_min = (B + C) % 60

if finish_hr >= 24:
    finish_hr -= 24

print(f"{finish_hr} {finish_min}")