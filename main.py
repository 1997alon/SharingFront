from login import open_login_window
from client import Client
from login import logged_in_username
if __name__ == "__main__":
    client = Client()
    open_login_window(client)
