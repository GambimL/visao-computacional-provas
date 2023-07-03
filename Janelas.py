from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk




def criar_gabarito():
    window = Tk()
    window.config(padx=10, pady=10)
    frames = []

    frame_text = Frame(window)
    frame_text.pack(side = 'top')
    imput = Entry(frame_text, width = 20)
    imput.pack()
    


    

    alternativas = ['A', 'B', 'C', 'D', 'E']
    frametop = Frame(window)
    frametop.pack(side='top')
    frame1 = Frame(frametop)
    frames.append(frame1)
    frame2 = Frame(frametop)
    frames.append(frame2)
    frame3 = Frame(frametop)
    frames.append(frame3)
    frame4 = Frame(frametop)
    frames.append(frame4)
    frame5 = Frame(frametop)
    frames.append(frame5)
    frame6 = Frame(frametop)
    frames.append(frame6)
    frame7 = Frame(frametop)
    frames.append(frame7)
    frame8 = Frame(frametop)
    frames.append(frame8)
    frame9 = Frame(frametop)
    frames.append(frame9)
    frame10 = Frame(frametop)
    frames.append(frame10)


    for k in range(10):
        frames[k].pack(side='left')
        var1 = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        label_questoe = Label(frames[k], text=f'Q{k+1}')
        label_questoe.pack(ipadx=1, padx=1)
        for i in range(5):
            c1 = Checkbutton(frames[k], 
                     text=alternativas[i], 
                     variable=var1[i], 
                     onvalue=1, 
                     offvalue=0)
            c1.pack()

    frames2 = []
    framebottom = Frame(window, bg = 'red')
    framebottom.pack(side='top')
    frame1_2 = Frame(framebottom)
    frames2.append(frame1_2)
    frame2_2 = Frame(framebottom)
    frames2.append(frame2_2)
    frame3_2 = Frame(framebottom)
    frames2.append(frame3_2)
    frame4_2 = Frame(framebottom)
    frames2.append(frame4_2)
    frame5_2 = Frame(framebottom)
    frames2.append(frame5_2)
    frame6_2 = Frame(framebottom)
    frames2.append(frame6_2)
    frame7_2 = Frame(framebottom)
    frames2.append(frame7_2)
    frame8_2 = Frame(framebottom)
    frames2.append(frame8_2)
    frame9_2 = Frame(framebottom)
    frames2.append(frame9_2)
    frame10_2 = Frame(framebottom)
    frames2.append(frame10_2)




    for k in range(10):
        frames2[k].pack(side='left')
        var1 = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        label_questoe = Label(frames2[k], text=f'Q{k+11}')
        label_questoe.pack(ipadx=1, padx=1)
        for i in range(5):
            c1 = Checkbutton(frames2[k], 
                     text=alternativas[i], 
                     variable=var1[i], 
                     onvalue=1, 
                     offvalue=0)
            c1.pack()
    


    


    


    window.mainloop()


def corrigir_provas():
    window = Tk()

    


    window.mainloop()

def dados():
    window = Tk()

    


    window.mainloop()