import tkinter as tk
from tkinter import font, messagebox


def open_messages_window(username, client, message_res):
    root = tk.Tk()
    root.title("📨 Your Messages")
    root.geometry("700x500")

    tk.Label(root, text=f"📬 Messages for {username}", font=("Arial", 16)).pack(pady=10)

    messages = message_res.get("messages", [])

    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for msg in messages:
        kind = msg.get("kind", "regular")
        status = msg.get("status", "read")
        topic = msg.get("topic", "N/A")
        time = msg.get("time", "Unknown Time")
        sender_id = msg.get("sender", "Unknown Sender")
        message_id = msg.get("messageID", -1)

        # Choose styles
        text_color = "black" if kind == "authorization" else "blue"
        weight = "bold" if status != "read" else "normal"
        label_font = font.Font(family="Arial", size=11, weight=weight)

        msg_text = f"[{kind.upper()}] From UserID {sender_id} about '{topic}' at {time}"

        def on_click_message(sender=sender_id, msg_id=message_id):
            client.open_a_message(username, sender, msg_id)
            opened = client.getRes()

            print(opened)
            if opened.get("success"):
                content = opened.get("messageContent", "(No content)")
                authorization = kind == "authorization"
                read_status = status != "read"

                # Navigate to openamessage.py
                root.destroy()
                from openamessage import open_message_window
                open_message_window(username, client, opened, authorization, read_status, sender, msg_id, message_res)

            else:
                print("Error in opening the message.")

        # Button to view the message
        btn = tk.Button(
            scrollable_frame,
            text=msg_text,
            fg=text_color,
            font=label_font,
            anchor="w",
            justify="left",
            wraplength=650,
            command=on_click_message
        )
        btn.pack(fill="x", padx=10, pady=4)

    # Back to menu button
    def back_to_menu():
        root.destroy()
        from menu import open_menu_window
        open_menu_window(client, message_res, username)

    tk.Button(root, text="🔙 Back to Menu", command=back_to_menu).pack(pady=10)

    root.mainloop()
