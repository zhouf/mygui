import tkinter as tk

window = tk.Tk()
window.title('My Listbox')
window.geometry('400x200')

def print_val(v):
    l.config(text='you have selected: ' + v)
    return

l = tk.Label(window,bg='yellow',width=30,height=2,text='Empty')
l.pack()

s = tk.Scale(window,label='try me',from_=5,to=25,orient=tk.HORIZONTAL,length=300,
             showvalue=False,tickinterval=5,resolution=0.1,command=print_val)
s.pack()

window.mainloop()