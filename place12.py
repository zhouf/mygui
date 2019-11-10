import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('400x300')

tk.Label(window,text='L').pack(side='left')
tk.Label(window,text='R').pack(side='right')
tk.Label(window,text='T').pack(side='top')
tk.Label(window,text='B').pack(side='bottom')

window.mainloop()