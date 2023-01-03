from tkinter import *
root = Tk()
T = Text(root, height = 20, width = 30, bg='blue', fg='red')
T.grid(row=10, column=0)
T.pack()
T.insert(END, 'ADHD BANK')
root.mainloop()