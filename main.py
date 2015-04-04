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