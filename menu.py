import tkinter as tk
from tkinter import messagebox


def open_menu_window(client, res, username):
    root = tk.Tk()
    root.title("Menu")
    root.geometry("600x400")

    # === Greeting and New Message Notification ===
    tk.Label(root, text=f"👋 Hello {username}!", font=("Arial", 16)).pack(pady=10)

    if res.get("success") and res.get("newMessages"):
        messagebox.showinfo("📩 New Messages", "You have new unread messages!")
        root.focus_force()

    # === Main Frame for layout ===
    main_frame = tk.Frame(root)
    main_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # === Left Panel Frame (Navigation Buttons) ===
    left_frame = tk.Frame(main_frame)
    left_frame.grid(row=0, column=0, rowspan=4, sticky="n")  # Adjusted to accommodate new button

    # My Topics Button
    def open_my_topics():
        root.destroy()
        from myTopics import open_my_topics_window
        open_my_topics_window(client, username)

    tk.Button(left_frame, text="📘 My Topics", command=open_my_topics, width=20).pack(pady=5)

    # Authorization Button
    def open_authorization():
        root.destroy()
        from authorization import open_authorization_window
        open_authorization_window(client, username)

    tk.Button(left_frame, text="🔐 Authorization", command=open_authorization, width=20).pack(pady=5)

    def open_update_topic():
        root.destroy()
        from updateTopic import open_update_topic_window  # Ensure updateTopic.py exists
        open_update_topic_window(client, username)

    tk.Button(left_frame, text="✏️ Update Topic", command=open_update_topic, width=20).pack(pady=5)

    # Messages Button
    def open_messages():
        client.get_messages(username)
        message_res = client.getRes()
        root.destroy()
        from messages import open_messages_window
        open_messages_window(username, client, message_res)

    tk.Button(left_frame, text="📨 Messages", command=open_messages, width=20).pack(pady=5)

    # Add Topic Button
    def open_add_topic():
        root.destroy()
        from addTopic import open_add_topic_window  # Ensure 'addTopic' module exists
        open_add_topic_window(client, username)

    tk.Button(left_frame, text="➕ Add Topic", command=open_add_topic, width=20).pack(pady=5)  # New Add Topic button

    # === Search Section ===
    tk.Label(main_frame, text="🔍 Search Topic:").grid(row=0, column=1, sticky="e", padx=5)
    entry_search = tk.Entry(main_frame, width=30)
    entry_search.grid(row=0, column=2, sticky="w", padx=5)

    result_label = tk.Label(main_frame, text="", wraplength=500, justify="left")
    result_label.grid(row=2, column=1, columnspan=2, pady=10)

    def handle_search():
        query = entry_search.get().strip()
        if not query:
            result_label.config(text="⚠️ Please enter a topic name.")
            return

        client.search_topic(username, query)
        res_one = client.getRes()

        if res_one.get("success"):
            client.get_topic_details(username, query)
            res_two = client.getRes()
            if res_two.get("success"):
                content = res_two.get("content", "No content")
                author = res_two.get("author", "Unknown")
                created_at = res_two.get("time", "Unknown time")
                result_text = f"📄 Content:\n{content}\n\n👤 Author: {author}\n🕒 Time: {created_at}"
            else:
                result_text = "❌ Failed to fetch topic details."
        else:
            result_text = "❌ Topic not found."

        result_label.config(text=result_text)

    tk.Button(main_frame, text="Search", command=handle_search, width=15).grid(row=1, column=2, pady=5, sticky="w")

    # === Back to Login Button ===
    def go_back_to_login():
        root.destroy()
        from login import open_login_window
        open_login_window(client)

    tk.Button(root, text="🔙 Back to Login", command=go_back_to_login).pack(side="bottom", pady=10)

    root.mainloop()
