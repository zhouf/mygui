import tkinter as tk

win = tk.Tk()
win.title('My first GUI')
win.geometry('400x300')

str = tk.StringVar()
hit = False

lable = tk.Label(win,textvariable=str ,bg='green',font=('Arial',12),width=25,height=3)

lable.pack()


def cmd():
    global hit
    print('Hello kitty',hit)
    if hit==False:
        str.set('You hit me')
    else:
        str.set('')
    hit = not hit

btn = tk.Button(win,text='Send Email',height=2,width=25,command=cmd)
btn.pack()

win.mainloop()
