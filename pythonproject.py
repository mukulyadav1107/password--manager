# Programmed By: Mukul Yadav (1/24/SET/BCS/372)

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Password Manager")
root.geometry("400x300")

MASTER_PASSWORD = "1234"

# ==============================
# SAVE PASSWORD
# ==============================

def save_password():
    site = site_entry.get()
    user = user_entry.get()
    pwd = pass_entry.get()

    with open("data.txt", "a") as file:
        file.write(f"Website: {site}\n")
        file.write(f"Username: {user}\n")
        file.write(f"Password: {pwd}\n")
        file.write("----------------------\n")

    messagebox.showinfo("Success", "Data Saved Successfully ✅")

# ==============================
# VIEW PASSWORDS (WITH SECURITY)
# ==============================

def view_passwords():

    def check():
        if pass_check.get() == MASTER_PASSWORD:
            view_win.destroy()

            show = Toplevel(root)
            show.title("Saved Passwords")
            show.geometry("400x300")

            try:
                with open("data.txt", "r") as file:
                    data = file.read()
            except:
                data = "No data found"

            Label(show, text="Saved Passwords", font=("Arial", 14)).pack(pady=10)
            Text(show, height=15, width=45).insert(END, data)

            text_box = Text(show, height=15, width=45)
            text_box.pack()
            text_box.insert(END, data)

        else:
            messagebox.showerror("Error", "Wrong Master Password ❌")

    view_win = Toplevel(root)
    view_win.title("Security Check")
    view_win.geometry("300x150")

    Label(view_win, text="Enter Master Password").pack(pady=10)
    pass_check = Entry(view_win, show="*")
    pass_check.pack(pady=5)

    Button(view_win, text="Submit", command=check).pack(pady=10)

# ==============================
# LOGIN FUNCTION
# ==============================

def login():
    if password_entry.get() == MASTER_PASSWORD:
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Error", "Wrong Password ❌")

# ==============================
# LOGIN UI
# ==============================

login_frame = Frame(root)

Label(login_frame, text="Login", font=("Arial", 20)).pack(pady=20)
Label(login_frame, text="Enter Master Password").pack()

password_entry = Entry(login_frame, show="*")
password_entry.pack(pady=10)

Button(login_frame, text="Login", command=login).pack()

login_frame.pack()

# ==============================
# MAIN UI
# ==============================

main_frame = Frame(root)

Label(main_frame, text="Add Password", font=("Arial", 16)).pack(pady=10)

Label(main_frame, text="Website").pack()
site_entry = Entry(main_frame)
site_entry.pack()

Label(main_frame, text="Username").pack()
user_entry = Entry(main_frame)
user_entry.pack()

Label(main_frame, text="Password").pack()
pass_entry = Entry(main_frame)
pass_entry.pack()

Button(main_frame, text="Save", command=save_password).pack(pady=10)
Button(main_frame, text="View Passwords", command=view_passwords).pack(pady=5)

# ==============================
# RUN
# ==============================

root.mainloop()