from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from random import randrange

root = Tk()
root.title('Gallows Game')


lb1 = Label(root, padx=10, pady=10, text='Gallows', font=('Comic Sans', 20))
lb1.grid(row=0,column=0, columnspan=3)

#word
bt = [
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
]

#grammata
bt1=[
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ']
]

btheart = [' ',' ',' ',' ',' ',' ']

imgA = ImageTk.PhotoImage(Image.open('A.jpg'))
imgB = ImageTk.PhotoImage(Image.open('B.jpg'))
imgC = ImageTk.PhotoImage(Image.open('C.jpg'))
imgD = ImageTk.PhotoImage(Image.open('D.jpg'))
imgE = ImageTk.PhotoImage(Image.open('E.jpg'))
imgF = ImageTk.PhotoImage(Image.open('F.jpg'))
imgG = ImageTk.PhotoImage(Image.open('G.jpg'))
imgH = ImageTk.PhotoImage(Image.open('H.jpg'))
imgI = ImageTk.PhotoImage(Image.open('I.jpg'))
imgJ = ImageTk.PhotoImage(Image.open('J.jpg'))
imgK = ImageTk.PhotoImage(Image.open('K.jpg'))
imgL = ImageTk.PhotoImage(Image.open('L.jpg'))
imgM = ImageTk.PhotoImage(Image.open('M.jpg'))
imgN = ImageTk.PhotoImage(Image.open('N.jpg'))
imgO = ImageTk.PhotoImage(Image.open('O.jpg'))
imgP = ImageTk.PhotoImage(Image.open('P.jpg'))
imgQ = ImageTk.PhotoImage(Image.open('Q.jpg'))
imgR = ImageTk.PhotoImage(Image.open('R.jpg'))
imgS = ImageTk.PhotoImage(Image.open('S.jpg'))
imgT = ImageTk.PhotoImage(Image.open('T.jpg'))
imgU = ImageTk.PhotoImage(Image.open('U.jpg'))
imgV = ImageTk.PhotoImage(Image.open('V.jpg'))
imgW = ImageTk.PhotoImage(Image.open('W.jpg'))
imgX = ImageTk.PhotoImage(Image.open('X.jpg'))
imgY = ImageTk.PhotoImage(Image.open('Y.jpg'))
imgZ = ImageTk.PhotoImage(Image.open('Z.jpg'))
imgheart = ImageTk.PhotoImage(Image.open('heart2.png'))
imgheart2 = ImageTk.PhotoImage(Image.open('heart233.png'))
imggallows = ImageTk.PhotoImage(Image.open('gallows2.png'))
imgline = ImageTk.PhotoImage(Image.open('line.jpg'))

#grammata
fr1 = Frame(root, padx=30, pady=20)
fr1.grid(row=2,column=2)

#kardies
fr2 = Frame(root, padx=30, pady=20)
fr2.grid(row=2,column=0)

# highlightbackground="blue", highlightthickness=2

lbgal = Label(root, image=imggallows)
lbgal.grid(row=2, column=1)

chr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
imaglist = [imgA, imgB, imgC, imgD, imgE, imgF, imgG, imgH, imgI, imgJ, imgK, imgL, imgM, imgN, imgO, imgP, \
            imgQ, imgR, imgS, imgT, imgU, imgV, imgW, imgX, imgY, imgZ]


def click(r,c,c1):
    global l, lose, thesi, word, lnew
    flag = False
    bt1[r][c].config(bg='red')
    #nea lista me ta grammata

    for i in range(len(l)):
        if l[i]==c1:
            if i==0:
                bt[0][i]['image'] = bt1[r][c]['image']
                lnew[i] = c1
            else:
                bt[0][i*2]['image'] = bt1[r][c]['image']
                lnew[i] = c1
            flag = True
            print(lnew)
        word1 = ''.join(lnew)
        if word == word1:
            messagebox.showinfo(title='Message', message=f"Bravo, you won!")


    if flag == False:
        btheart[thesi].configure(image=imgheart2)
        thesi -=1
        if thesi == -1 :
            messagebox.showinfo(title='Message', message=f"You Lost. The hidden word is {word}")




chr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
imaglist = [imgA, imgB, imgC, imgD, imgE, imgF, imgG, imgH, imgI, imgJ, imgK, imgL, imgM, imgN, imgO, imgP, imgQ, imgR, imgS, imgT, imgU, imgV, imgW, imgX, imgY, imgZ]

fr3 = Frame(root)
fr3.grid(row=3, column=0, columnspan=3)

lbkeno = Label(fr2)
lbkeno.grid(row=1, column=1)

lbkeno2 = Label(fr2)
lbkeno2.grid(row=2, column=1)

def reset():
    global lose, l, bt, bt1, thesi, word, lnew
    thesi = 4
    lose =0
    k = 0
    for i in range(1, 6, 1):
        for j in range(1, 6, 1):
            bt1[i][j] = Button(fr1, image=imaglist[k], padx=79, pady=79,
                               command=lambda r=i, c=j, c1=chr[k]: click(r, c, c1))
            bt1[i][j].grid(row=i, column=j)
            k += 1
    bt1[6][3] = Button(fr1, image=imaglist[k], padx=74, pady=61, command=lambda r=6, c=3, c1=chr[k]: click(r, c, c1))
    bt1[6][3].grid(row=6, column=3)

    for i in range(5):
        btheart[i] = Label(fr2, image= imgheart)
        btheart[i].grid(row=3, column=i)

    #pano megalo
    for i in range(0,13,2):
        print(i)
        bt[0][i] = Label(fr3, padx=40, pady=7)
        bt[0][i].grid(row=0, column=i)
    #pano mikro
    for i in range(1, 13, 2):
        bt[0][i] = Label(fr3, padx=20, pady=7)
        bt[0][i].grid(row=0, column=i)
    #kato megalo
    for i in range(0, 13, 2):
        bt[1][i] = Label(fr3, padx=40, pady=0.0005)
        bt[1][i].grid(row=1, column=i)
    #kato mikro
    for i in range(1, 13, 2):
        bt[1][i] = Label(fr3, padx=20, pady=0.0005  )
        bt[1][i].grid(row=1, column=i)


    with open('words.txt', 'r') as f:
        lista = f.readlines()

    word = lista[randrange(len(lista))].upper()
    while True:
        if len(word) <= 7:
            break
        else:
            word = lista[randrange(len(lista))].upper()

    l= list(word)
    del l[len(l)-1]
    word = ''.join(l)
    print(word)

    #nea lista me ta grammata poy dinei o xristis
    lnew = []
    for j in range(len(word)):
        lnew.append(' ')

    for i in range(0,2*len(word)-1,2):
        bt[1][i] = Label(fr3, padx=20, pady=1, image = imgline)
        bt[1][i].grid(row=1, column=i)



bt_reset = Button (fr2, padx=20, pady=10, text='New Game', bg='violet', command=reset)
bt_reset.grid(row=0,column=0, columnspan=5)

reset()
root.mainloop()