
import socket
import json

# Encoding: convert characters to ASCII numbers with spaces
def ascii_encrypt(text):
    return ' '.join(str(ord(char)) for char in text) + ' ' + str(0)

# Decoding: convert ASCII numbers back to characters
def ascii_decrypt(ascii_str):
    parts = ascii_str.strip().split()
    decoded = ''.join(chr(int(part)) for part in parts if part.isdigit() and int(part) != 0)
    return decoded

def recv_until_null(sock):
    data = b''
    while True:
        chunk = sock.recv(1)
        if not chunk or chunk == b'\0':
            break
        data += chunk
    return data.decode('utf-8')


class Client:
    def __init__(self, host='127.0.0.1', port=12345):
        self.server_address = (host, port)
        self.res = None

    def send_request(self, action, arguments):
        message = {
            "action": action,
            "arguments": arguments
        }
        json_str = json.dumps(message)
        encrypted = ascii_encrypt(json_str)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(self.server_address)
                sock.sendall(encrypted.encode('utf-8'))

                response_str = recv_until_null(sock)
                decrypted_message = ascii_decrypt(response_str)

                try:
                    self.res = json.loads(decrypted_message)
                    print(self.res)
                except json.JSONDecodeError:
                    print("❌ Failed to decode JSON from server response.")
                    print("🔓 Raw decrypted message:", decrypted_message)

        except Exception as e:
            print("❌ Error:", str(e))


    # Define actions as convenience methods
    def sign_up(self, username, password, email):
        self.send_request("signUp", {"username": username, "password": password, "email": email})

    def login(self, username, password):
        self.send_request("login", {"username": username, "password": password})

    def add_topic(self, username, topicName, author, content):
        self.send_request("addTopic", {"username": username, "topicName": topicName, "author": author, "content": content})

    def search_topic(self, username, topicName):
        self.send_request("searchTopic", {"username": username, "topicName": topicName})

    def get_topic_details(self, username, topicName):
        self.send_request("getTopicDetails", {"username": username, "topicName": topicName})

    def get_all_topics(self, username):
        self.send_request("getAllTopics", {"username": username})

    def get_user_topics(self, username):
        self.send_request("getUserTopics", {"username": username})

    def check_authorization_topic(self, username, topicName):
        self.send_request("checkAuthorizationTopic", {"username": username, "topicName": topicName})

    def get_authorization_topics(self, username):
        self.send_request("getAuthorizationTopics", {"username": username})

    def get_messages(self, username):
        self.send_request("getMessages", {"username": username})

    def open_a_message(self, username, sender, messageID):
        self.send_request("openAMessage", {"username": username, "sender": sender, "messageID": messageID})

    def update_topic(self, username, topicName, content):
        self.send_request("updateTopic", {"username": username, "topicName": topicName, "content": content})

    def approve_authorization_topic(self, username, sender, messageID, approved):
        self.send_request("approveAuthorizationTopic", {"username": username, "sender": sender, "messageID": messageID, "approved": approved})

    def ask_for_authorization_topic(self, username, topicName):
        self.send_request("askForAuthorizationTopic", {"username": username, "topicName": topicName})

    def menu(self, username):
        self.send_request("menu", {"username": username})

    def getRes(self):
        return self.res

def print_response(response):
    print("\n📩 Server response:")
    print(json.dumps(response, indent=2))

