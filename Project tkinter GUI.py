from tkinter import *
root = Tk()
root.title('ADHD BANK')
root.config(bg='#000428')
T = Label(root, text='ADHD BANK', font=("Bold",150),bg='#000428', fg='#B0750F')
T.place(relx=0.5,rely=0.5,anchor='center')
T.pack()
L = Label(root, text='LOGIN' ,font=("Bold",40),fg='#42C665',bg='#000428')
L.pack()
username_label = Label(root, text="Enter username or account number:",width=40,bg='#000428',font=("Bold",25),fg='#B0750F')
username_text = Entry(width=50)

password_label = Label(root, text="Password:",width=40,bg='#000428',font=("Bold",25),fg='#B0750F')
password_text = Entry(show = "*",width=50)

login_button = Button(text = "LOGIN",width=25,bg='#42C665',font=("Bold"))

username_label.place(relx=0.5,rely=0.4,anchor='center')
username_text.place(relx=0.5,rely=0.45,anchor='center')
password_label.place(relx=0.5,rely=0.5,anchor='center')
password_text.place(relx=0.5,rely=0.55,anchor='center')
login_button.place(relx=0.5,rely=0.6,anchor='center')

forgotpsswd_button = Button(text= "Forgot password",width=25,font=("Bold"),fg='red',bg='#000428')
forgotpsswd_button.place(relx=0.5,rely=0.67,anchor='center')

register_button = Button(text="Click here to register", width=25,bg='#000428',fg='#D8EE6C',font=("Bold"))


register_button.place(relx=0.5,rely=0.8,anchor='center')
root.mainloop()
#completed login page
#end of code