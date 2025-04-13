import tkinter as tk
from tkinter import messagebox

def open_authorization_window(client, username):
    root = tk.Tk()
    root.title("Authorization Page")
    root.geometry("650x500")

    # Greeting
    greeting = tk.Label(root, text=f"🔐 Authorization Center for {username}", font=("Arial", 14))
    greeting.grid(row=0, column=0, columnspan=3, pady=10)

    # Results display area
    result_label = tk.Label(root, text="", wraplength=600, justify="left", anchor="w")
    result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    # --- Button: Get All Topics ---
    def fetch_all_topics():
        client.get_all_topics(username)
        res = client.getRes()
        if res.get("success"):
            topics = res.get("topics", [])
            text = "\n".join([f"📘 {t['topic']} | 👤 {t['author']} | 🕒 {t['time']}" for t in topics])
            result_label.config(text=f"All Topics:\n\n{text}")
        else:
            result_label.config(text="❌ Failed to fetch topics.")

    tk.Button(root, text="📚 Get All Topics", command=fetch_all_topics).grid(row=1, column=0, padx=10, pady=5)

    # --- Button: Get Authorized Topics ---
    def fetch_authorized_topics():
        client.get_authorization_topics(username)
        res = client.getRes()
        if res.get("success"):
            topics = res.get("topics", [])
            text = "\n".join([f"✅ {t['topic']}" for t in topics])
            result_label.config(text=f"Authorized Topics:\n\n{text}")
        else:
            result_label.config(text="❌ Failed to fetch authorized topics.")

    tk.Button(root, text="🛡️ Get Authorized Topics", command=fetch_authorized_topics).grid(row=1, column=1, padx=10, pady=5)

    # --- Check Authorization ---
    tk.Label(root, text="Check Topic Authorization:").grid(row=2, column=0, columnspan=2, pady=5)
    entry_topic_name = tk.Entry(root, width=40)
    entry_topic_name.grid(row=3, column=0, columnspan=2, padx=10)

    def check_topic_auth():
        topic_name = entry_topic_name.get()
        if not topic_name:
            messagebox.showwarning("Input Needed", "Please enter a topic name.")
            return
        client.check_authorization_topic(username, topic_name)
        res = client.getRes()
        if res.get("success"):
            result_label.config(text=f"✅ You are authorized for topic: '{topic_name}'")
        else:
            result_label.config(text=f"❌ Authorization failed: {res.get('error', 'Unknown error')}")
            answer = messagebox.askyesno("Request Authorization",
                                         f"You are not authorized for '{topic_name}'.\nWould you like to request access?")
            if answer:
                client.ask_for_authorization_topic(username, topic_name)
                messagebox.showinfo("Request Sent",
                                    f"Your request for authorization to '{topic_name}' has been sent.\nYou'll need to wait for approval.")
            root.focus_force()

    tk.Button(root, text="Check Authorization", command=check_topic_auth).grid(row=3, column=2, padx=10)

    # --- Back to Menu ---
    def go_back_to_menu():
        root.destroy()
        from menu import open_menu_window
        res = {"success": False}  # or fetch again if needed
        open_menu_window(client, res, username)

    tk.Button(root, text="⬅️ Back to Menu", command=go_back_to_menu).grid(row=6, column=0, columnspan=3, pady=20)

    root.mainloop()
