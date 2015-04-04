import random
import tkinter as tk
from tkinter import messagebox
import sys


def main():
    def button_click(event):
        nonlocal closed
        i = event.x // 50
        j = event.y // 50
        if field[i][j] == 9:
            for ii in range(10):
                for jj in range(10):
                    if field[ii][jj] < 0:
                        c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[-field[ii][jj] - 1])
                    else:
                        c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[field[ii][jj]])
            for ii in range(10):
                c.create_line(ii * 50, 0, ii * 50, 500)
                c.create_line(0, ii * 50, 500, ii * 50)

            messagebox.showinfo(message='Game over!')
            sys.exit(0)

        if field[i][j] < 0:
            return

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
            for ii in range(10):
                for jj in range(10):
                    if field[ii][jj] < 0:
                        c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[-field[ii][jj] - 1])
                    else:
                        c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[' '])
            for ii in range(10):
                c.create_line(ii * 50, 0, ii * 50, 500)
                c.create_line(0, ii * 50, 500, ii * 50)

            if closed == 0:
                messagebox.showinfo(message='Winner!')
                sys.exit()
            return

        field[i][j] = -field[i][j] - 1
        closed -= 1
        for ii in range(10):
            for jj in range(10):
                if field[ii][jj] < 0:
                    c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[-field[ii][jj] - 1])
                else:
                    c.create_image(ii * 50, jj * 50, anchor=tk.NW, image=imgs[' '])
        for ii in range(10):
            c.create_line(ii * 50, 0, ii * 50, 500)
            c.create_line(0, ii * 50, 500, ii * 50)
        if closed == 0:
            messagebox.showinfo(message='Winner!')
            sys.exit()

    root = tk.Tk()
    c = tk.Canvas(root, width=500, height=500)
    c.pack()
    imgs = {i: tk.PhotoImage(file='imgs/{}.png'.format(i)) for i in range(10)}
    imgs[9] = tk.PhotoImage(file='imgs/bomb.png')
    imgs[' '] = tk.PhotoImage(file='imgs/empty.png')

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

    for i in range(10):
        for j in range(10):
            c.create_image(i * 50, j * 50, anchor=tk.NW, image=imgs[' '])
    for i in range(10):
        c.create_line(i * 50, 0, i * 50, 500)
        c.create_line(0, i * 50, 500, i * 50)
    closed = 96
    c.bind('<Button-1>', button_click)
    root.mainloop()

if __name__ == '__main__':
    main()