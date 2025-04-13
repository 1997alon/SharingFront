import tkinter as tk

def open_topic_window(client, username, topic_name, res_topic):
    root = tk.Tk()
    root.title(f"📖 Topic: {topic_name}")
    root.geometry("600x400")

    content = res_topic.get("content", "No content available.")
    author = res_topic.get("author", "Unknown")
    time = res_topic.get("time", "Unknown")

    tk.Label(root, text=f"📌 {topic_name}", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text=f"👤 {author} | 🕒 {time}", font=("Arial", 10)).pack(pady=5)

    text_box = tk.Text(root, wrap="word", height=15, width=70)
    text_box.insert("1.0", content)
    text_box.config(state="disabled")
    text_box.pack(padx=10, pady=10)

    def go_back():
        root.destroy()
        from myTopics import open_my_topics_window
        open_my_topics_window(client, username)

    tk.Button(root, text="🔙 Back to Topics", command=go_back).pack(pady=10)

    root.mainloop()
