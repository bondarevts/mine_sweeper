import random


def main():
    field = [[0] * 10 for _ in range(10)]
    for i in range(4):
        field[random.randrange(10)][random.randrange(10)] = -1
    for i in range(10):
        for j in range(10):
            if field[i][j] == 0:
                print(' ', end='')
            elif field[i][j] == -1:
                print('*', end='')
            else:
                print(field[i][j], end='')
        print()

    for i in range(10):
        for j in range(10):
            if field[i][j] == -1:
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < 10 and 0 <= jj < 10 and field[ii][jj] != -1:
                            field[ii][jj] += 1

    print('-' * 10)
    for i in range(10):
        for j in range(10):
            if field[i][j] == 0:
                print(' ', end='')
            elif field[i][j] == -1:
                print('*', end='')
            else:
                print(field[i][j], end='')
        print()


if __name__ == '__main__':
    main()