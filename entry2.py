import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('400x200')

e = tk.Entry(window,show='*')
e.pack()


def pointcmd():
    str = e.get()
    print('insert point',str)
    t.insert('insert',str)

# 怎么改变Text中的文本内容

def endcmd():
    str = e.get()
    print('insert end',str)
    t.insert('end',str)

btn1=tk.Button(window,text='insert point',width=25,command=pointcmd)
btn1.pack()

btn2=tk.Button(window,text='insert end',width=25,command=endcmd)
btn2.pack()

t = tk.Text(window,height=2)
t.pack()


window.mainloop()