from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title('Tic Tac Toe')

img1 = ImageTk.PhotoImage(Image.open('tic3.jpg'))
imgx = ImageTk.PhotoImage(Image.open('bx.jpg'))
imgo = ImageTk.PhotoImage(Image.open('bo.jpg'))
imgb = ImageTk.PhotoImage(Image.open('blue.jpg'))

but = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

lb1 = Label(root,image=img1)
lb1.grid(row=0, column=0, columnspan=3)

frm = Frame(root)
frm.grid(row=1, column=0, columnspan=3)


def disab():
    for r in range(3):
        for c in range(3):
            but[r][c].config(state=DISABLED)


def winner(r, c):
    global flag, flag_win

    if but[r][0]['image'] == but[r][1]['image'] and but[r][1]['image'] == but[r][2]['image'] and but[r][2]['image'] != fb:
        disab()
        flag_win = True
        but[r][0].config(bg='lime')
        but[r][1].config(bg='lime')
        but[r][2].config(bg='lime')
        if flag == True:
            messagebox.showinfo(title='Message', message='Congratulations, X wins!')
        else:
            messagebox.showinfo(title='Message', message='Congratulations, O wins!')

    if but[0][c]['image'] == but[1][c]['image'] and but[1][c]['image'] == but[2][c]['image'] and but[2][c]['image'] != fb:
        disab()
        flag_win = True
        but[0][c].config(bg='lime')
        but[1][c].config(bg='lime')
        but[2][c].config(bg='lime')
        if flag == True:
            messagebox.showinfo(title='Message', message='Congratulations, X wins!')
        else:
            messagebox.showinfo(title='Message', message='Congratulations, O wins!')

    if but[0][0]['image'] == but[1][1]['image'] and but[1][1]['image'] == but[2][2]['image'] and but[2][2]['image'] != fb:
        disab()
        flag_win = True
        but[0][0].config(bg='lime')
        but[1][1].config(bg='lime')
        but[2][2].config(bg='lime')
        if flag == True:
            messagebox.showinfo(title='Message', message='Congratulations, X wins!')
        else:
            messagebox.showinfo(title='Message', message='Congratulations, O wins!')

    if but[2][0]['image'] == but[1][1]['image'] and but[1][1]['image'] == but[0][2]['image'] and but[0][2]['image'] != fb:
        disab()
        flag_win = True
        but[2][0].config(bg='lime')
        but[1][1].config(bg='lime')
        but[0][2].config(bg='lime')
        if flag == True:
            messagebox.showinfo(title='Message', message='Congratulations, X wins!')
        else:
            messagebox.showinfo(title='Message', message='Congratulations, O wins!')


def click(r, c):
    global flag
    global count, fo, fx

    if but[r][c]['image'] == fb and flag == True:
        but[r][c].config(image=imgx)
        fx = but[r][c]['image']
        winner(r, c)
        flag = False
        count += 1

    if but[r][c]['image'] == fb and flag == False:
        but[r][c].config(image=imgo)
        fo = but[r][c]['image']
        winner(r, c)
        flag = True
        count += 1

    if count == 9 and flag_win == False:
        disab()
        messagebox.showinfo(title='Message', message='No Winner - Tie')


def rest():
    global flag, flag_win, count, fb
    flag = True
    count = 0
    flag_win = False
    for r in range(3):
        for c in range(3):
            but[r][c] = Button(frm, padx=57, pady=46, image= imgb, command=lambda row=r, column=c: click(row, column))
            but[r][c].grid(row=r, column=c)

    fb = but[0][0]['image']



button_reset = Button(root, text='New Game',bg='lime', padx=10, pady=10, command=rest)
button_reset.grid(row=2, column=1)

rest()
root.mainloop()
