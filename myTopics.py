import tkinter as tk
from tkinter import messagebox

def open_my_topics_window(client, username):
    root = tk.Tk()
    root.title("My Topics")
    root.geometry("600x500")

    tk.Label(root, text="📚 Your Topics", font=("Arial", 16)).pack(pady=10)

    # Frame to hold the topic buttons
    topics_frame = tk.Frame(root)
    topics_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def show_my_topics():
        client.get_user_topics(username)
        topics_res = client.getRes()

        for widget in topics_frame.winfo_children():
            widget.destroy()

        if topics_res.get("success"):
            topics = topics_res.get("topics", [])
            if not topics:
                tk.Label(topics_frame, text="📭 No topics found.").pack()
                return

            for i, topic in enumerate(topics):
                topic_name = topic.get("topic", "Unknown")
                author = topic.get("author", "Unknown")
                time = topic.get("time", "Unknown time")

                # Display topic name, author, time
                topic_info = f"• {topic_name}\n  👤 {author} | 🕒 {time}"
                tk.Label(topics_frame, text=topic_info, justify="left", anchor="w").grid(row=i, column=0, sticky="w", padx=5, pady=5)

                # View Button
                def view_topic(t=topic_name):  # bind current topic name
                    client.get_topic_details(username, t)
                    res_topic = client.getRes()
                    if res_topic.get("success"):
                        root.destroy()
                        from openATopic import open_topic_window
                        open_topic_window(client, username, t, res_topic)
                    else:
                        messagebox.showerror("❌ Error", res_topic.get("error", "Failed to fetch topic details."))

                tk.Button(topics_frame, text="View", command=view_topic).grid(row=i, column=1, padx=5, pady=5)

        else:
            tk.Label(topics_frame, text="❌ Failed to fetch your topics.").pack()

    show_my_topics()

    def go_back():
        root.destroy()
        from menu import open_menu_window
        open_menu_window(client, {}, username)

    tk.Button(root, text="🔙 Back to Menu", command=go_back).pack(pady=10)

    root.mainloop()
