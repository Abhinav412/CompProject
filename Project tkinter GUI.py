from tkinter import *
root = Tk()
root.title('ADHD BANK')
root.config(bg='red')
T = Label(root, text='ADHD BANK', font=("Bold",150),bg='red', fg='blue')
T.place(relx=0.5,rely=0.5,anchor='center')
T.pack()
L = Label(root, text='LOGIN' ,font=("Bold",40),fg='green',bg='red')
L.pack()
username_label = Label(root, text="Enter username or account number:",width=40,bg='red',font=("Bold"))
username_text = Entry(width=40)

password_label = Label(root, text="Password:",width=40,bg='red',font=("Bold"))
password_text = Entry(show = "*",width=40)

login_button = Button(text = "LOGIN",width=25,bg='green',font=("Bold"))

username_label.pack()
username_text.pack()
password_label.pack()
password_text.pack()
login_button.place(relx=0.5,rely=0.55,anchor='center')

forgotpsswd_button = Button(text= "Forgot password",width=25,font=("Bold"))
forgotpsswd_button.place(relx=0.5,rely=0.6,anchor='center')

R = Label(root, text="Register" ,font=("Bold",40),bg='red',fg='indigo')
register_button = Button(text="Click here to register", width=25,bg='blue',fg='black',font=("Bold"))

R.place(relx=0.5,rely=0.7,anchor='center')
register_button.place(relx=0.5,rely=0.8,anchor='center')
root.mainloop()