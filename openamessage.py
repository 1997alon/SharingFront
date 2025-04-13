import tkinter as tk
from tkinter import messagebox


def open_message_window(username, client, opened, authorization, read_status, sender, message_id, message_res):
    root = tk.Tk()
    root.title("📨 Message Details")
    root.geometry("700x500")

    # Message header
    tk.Label(root, text=f"📬 Message from UserID {sender}", font=("Arial", 16)).pack(pady=10)

    content = opened.get("messageContent", "(No content)")
    time = opened.get("time", "Unknown Time")
    topic = opened.get("topic", "N/A")

    # Display message content
    tk.Label(root, text=f"📝 Topic: {topic}", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(root, text=f"🕒 Time: {time}", font=("Arial", 12)).pack(pady=5)
    tk.Label(root, text=f"📄 Content: {content}", font=("Arial", 12), wraplength=650, justify="left").pack(pady=10)

    # Only show approve/reject buttons if it's an authorization request and unread
    print(opened.get("answered"))
    if authorization and opened.get("answered") == "none":
        def approve():
            client.approve_authorization_topic(username, sender, message_id, True)
            result = client.getRes()
            if result.get("success"):
                # Replace buttons with approval message
                approve_button.pack_forget()
                reject_button.pack_forget()
                tk.Label(root, text="✅ Authorization Approved!", font=("Arial", 14, "bold"), fg="green").pack(pady=10)
            else:
                messagebox.showerror("Error", "Failed to approve authorization.")

        def reject():
            client.approve_authorization_topic(username, sender, message_id, False)
            result = client.getRes()
            if result.get("success"):
                # Replace buttons with rejection message
                approve_button.pack_forget()
                reject_button.pack_forget()
                tk.Label(root, text="❌ Authorization Rejected!", font=("Arial", 14, "bold"), fg="red").pack(pady=10)
            else:
                messagebox.showerror("Error", "Failed to reject authorization.")

        # Buttons for approve/reject
        approve_button = tk.Button(root, text="✅ Approve", command=approve, width=15)
        approve_button.pack(pady=5)

        reject_button = tk.Button(root, text="❌ Reject", command=reject, width=15)
        reject_button.pack(pady=5)

    # Back to messages button
    def back_to_messages():
        root.destroy()
        # Ensure that 'messages' is correctly imported from the file containing the function open_messages_window
        try:
            from messages import open_messages_window
            open_messages_window(username, client, message_res)
        except ImportError:
            messagebox.showerror("Error", "Could not import messages window.")

    tk.Button(root, text="🔙 Back to Messages", command=back_to_messages).pack(pady=10)

    root.mainloop()
