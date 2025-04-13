import tkinter as tk
from tkinter import messagebox

def open_add_topic_window(client, username):
    root = tk.Tk()
    root.title("Add Topic")
    root.geometry("500x400")

    # === Labels and Entry fields ===
    tk.Label(root, text="📝 Add a New Topic", font=("Arial", 16)).pack(pady=10)

    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Topic Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_topic_name = tk.Entry(form_frame, width=40)
    entry_topic_name.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Author:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_author = tk.Entry(form_frame, width=40)
    entry_author.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Content:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
    text_content = tk.Text(form_frame, width=30, height=10)
    text_content.grid(row=2, column=1, pady=5)

    # === Submit Button ===
    def submit_topic():
        topic_name = entry_topic_name.get().strip()
        author = entry_author.get().strip()
        content = text_content.get("1.0", tk.END).strip()

        if not topic_name or not author or not content:
            messagebox.showwarning("⚠️ Missing Fields", "All fields must be filled out.")
            return

        # Send data to server using client
        client.add_topic(username, topic_name, author, content)
        res = client.getRes()

        if res.get("success"):
            messagebox.showinfo("✅ Success", "Topic added successfully!")
            root.destroy()
            from menu import open_menu_window
            open_menu_window(client, res, username)
        else:
            messagebox.showerror("❌ Error", res.get("arguments", "Unknown error"))

    tk.Button(root, text="➕ Submit Topic", command=submit_topic, width=20).pack(pady=15)

    # === Back to Menu Button ===
    def back_to_menu():
        root.destroy()
        from menu import open_menu_window
        open_menu_window(client, {}, username)

    tk.Button(root, text="🔙 Back to Menu", command=back_to_menu).pack()

    root.mainloop()
