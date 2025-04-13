# login.py
import tkinter as tk
from tkinter import messagebox

logged_in_username = None  # 🌍 Global variable to store username


def open_login_window(client):
    global logged_in_username  # make it writable from inside the function

    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        client.login(username, password)
        res = client.getRes()
        print(res)
        if res and res.get("success"):
            logged_in_username = username
            root.destroy()

            # ✅ Now call the menu and check for messages
            client.menu(username)
            menu_res = client.getRes()
            if menu_res.get("newMessages"):
                from menu import open_menu_window
                open_menu_window(client, menu_res, logged_in_username)
            else:
                from menu import open_menu_window
                open_menu_window(client, menu_res, logged_in_username)
        else:
            messagebox.showerror("Login Failed", res.get("error", "Unknown error"))

    def go_to_signup():
        root.destroy()
        from signup import open_signup_window
        open_signup_window(client)

    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(root, text="Login", command=handle_login).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Sign Up", command=go_to_signup).grid(row=3, column=0, columnspan=2)

    # 🚪 Exit Button to close the window
    tk.Button(root, text="Exit", command=root.destroy).grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()
