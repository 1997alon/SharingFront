# signup.py
import tkinter as tk
from tkinter import messagebox

def open_signup_window(client):
    def handle_signup():
        username = entry_username.get()
        password = entry_password.get()
        email = entry_email.get()

        client.sign_up(username, password, email)
        res = client.res
        print(res)
        if res and res.get("success"):
            messagebox.showinfo("Success", "User created successfully!")
            root.destroy()
            from login import open_login_window  # ⬅ moved import here
            open_login_window(client)
        else:
            messagebox.showerror("Error", res.get("error", "Failed to sign up"))

    def go_back_to_login():
        root.destroy()
        from login import open_login_window  # ⬅ moved import here
        open_login_window(client)

    root = tk.Tk()
    root.title("Sign Up")

    tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
    entry_email = tk.Entry(root)
    entry_email.grid(row=2, column=1)

    tk.Button(root, text="Create User", command=handle_signup).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Login", command=go_back_to_login).grid(row=4, column=0, columnspan=2)

    root.mainloop()
