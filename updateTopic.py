import tkinter as tk
from tkinter import messagebox

def open_update_topic_window(client, username):
    root = tk.Tk()
    root.title("Update Topic")
    root.geometry("600x400")

    tk.Label(root, text="✏️ Update a Topic", font=("Arial", 16)).pack(pady=10)

    # Topic name input
    tk.Label(root, text="Topic Name:").pack()
    entry_topic_name = tk.Entry(root, width=50)
    entry_topic_name.pack(pady=5)

    # New content input
    tk.Label(root, text="New Content:").pack()
    text_content = tk.Text(root, height=10, width=60)
    text_content.pack(pady=5)

    # Update function
    def update_topic():
        topic_name = entry_topic_name.get().strip()
        content = text_content.get("1.0", tk.END).strip()

        if not topic_name or not content:
            messagebox.showwarning("⚠️ Input Error", "Both topic name and content are required.")
            return

        client.update_topic(username, topic_name, content)
        res = client.getRes()

        if res.get("success"):
            messagebox.showinfo("✅ Success", f"Topic '{topic_name}' updated successfully!")
        else:
            messagebox.showerror("❌ Failed", f"Failed to update topic. Reason: {res.get('error', 'Unknown error')}")

    tk.Button(root, text="Update", command=update_topic, width=20).pack(pady=10)

    # Go back to menu
    def go_back():
        root.destroy()
        from menu import open_menu_window
        open_menu_window(client, {}, username)

    tk.Button(root, text="🔙 Back to Menu", command=go_back).pack(pady=5)

    root.mainloop()
