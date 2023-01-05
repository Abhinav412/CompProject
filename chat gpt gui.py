import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Bank Management System")

# Create a label and text box for the username
username_label = tk.Label(text="Username:")
username_text = tk.Entry()

# Create a label and text box for the password
password_label = tk.Label(text="Password:")
password_text = tk.Entry(show="*")

# Create a login button
login_button = tk.Button(text="Login")
# Place the widgets in the window
username_label.pack()
username_text.pack()
password_label.pack()
password_text.pack()
login_button.pack()

# Run the Tkinter event loop
window.mainloop()
