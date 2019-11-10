import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title('My window')
window.geometry('400x300')

def cmd():
    tk.messagebox.showinfo('title','This is the message')
    # print(tk.messagebox.askquestion('Question','Is that right?'))
    # print(tk.messagebox.askyesno('YesOrNo','Question.....'))
    # print(tk.messagebox.askyesnocancel('YesNoCandel','Question.....'))
    print(tk.messagebox.askretrycancel('askretrycancel','Question.....'))

    return

tk.Button(window,text='Button A',command=cmd).pack()

window.mainloop()