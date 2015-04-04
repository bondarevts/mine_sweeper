import random


def main():
    field = [[0] * 10 for _ in range(10)]
    for i in range(4):
        field[random.randrange(10)][random.randrange(10)] = 9

    for i in range(10):
        for j in range(10):
            if field[i][j] == 9:
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < 10 and 0 <= jj < 10 and field[ii][jj] != 9:
                            field[ii][jj] += 1

    print('-'*12)
    for i in range(10):
        print('|', end='')
        for j in range(10):
            if field[i][j] >= 0:
                print(' ', end='')
            elif field[i][j] == -1:
                print('_', end='')
            else:
                print(-field[i][j] - 1, end='')
        print('|')
    print('-'*12)

    closed = 96

    while closed:
        user_step = input('Input new step: ')
        parts = user_step.split()
        i = int(parts[0])
        j = int(parts[1])

        if field[i][j] == 9:
            print('Game over!')
            print('-'*12)
            for i in range(10):
                print('|', end='')
                for j in range(10):
                    if field[i][j] < 0:
                        field[i][j] = -field[i][j] + 1
                    if field[i][j] == 9:
                        print('*', end='')
                    elif field[i][j] == 0:
                        print(' ', end='')
                    else:
                        print(field[i][j], end='')
                print('|')
            print('-'*12)
            break
        if field[i][j] < 0:
            continue

        if field[i][j] == 0:
            check_pos = [(i, j)]
            while check_pos:
                last = check_pos.pop()
                ci = last[0]
                cj = last[1]
                if 0 <= ci < 10 and 0 <= cj < 10:
                    if field[ci][cj] == 0:
                        check_pos.extend((ii, jj) for ii in range(ci-1, ci + 2) for jj in range(cj-1, cj+2) if not (ci == ii and cj == jj))
                    if field[ci][cj] >= 0:
                        field[ci][cj] = -field[ci][cj] - 1
                        closed -= 1
            print('-'*12)
            for i in range(10):
                print('|', end='')
                for j in range(10):
                    if field[i][j] >= 0:
                        print(' ', end='')
                    elif field[i][j] == -1:
                        print('_', end='')
                    else:
                        print(-field[i][j] - 1, end='')
                print('|')
            print('-'*12)
            continue

        field[i][j] = -field[i][j] - 1
        closed -= 1

        print('-'*12)
        for i in range(10):
            print('|', end='')
            for j in range(10):
                if field[i][j] >= 0:
                    print(' ', end='')
                elif field[i][j] == -1:
                    print('_', end='')
                else:
                    print(-field[i][j] - 1, end='')
            print('|')
        print('-'*12)
    else:
        print('Winner!')


if __name__ == '__main__':
    main()