T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrot_field = list(map(int, input().split()))

    carrots = 0
    carrot_idx = 0

    for i in range(N):
        carrots = max(carrot_field)
        if carrots == carrot_field[i]:
            carrot_idx = i + 1
            break

    print('#{} {} {}'.format(tc, carrot_idx, carrots))