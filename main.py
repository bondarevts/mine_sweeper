import random


def main():
    field = [[None] * 10 for _ in range(10)]
    for i in range(4):
        field[random.randrange(10)][random.randrange(10)] = -1
    for i in range(10):
        for j in range(10):
            if field[i][j] is None:
                print(' ', end='')
            elif field[i][j] == -1:
                print('*', end='')
            else:
                print(field[i][j], end='')
        print()

if __name__ == '__main__':
    main()