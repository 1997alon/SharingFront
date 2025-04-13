# 🖥️ Sharing App - Frontend

👉 Go to the **backend repository**: [SharingApp-Backend](https://github.com/1997alon/SharingApp-Backend)

---

## ❓ What is this project?

**Sharing App** is a collaborative platform inspired by Wikipedia, but with enhanced control and security:

- Users can **create unique topics**, **upload content**, and **edit** only the topics they're authorized to.
- Topics are **publicly viewable**, but **editing is permission-based**.
- The platform includes a built-in **authorization system** and **messaging system**.
- Only registered users can interact with the system and content.

This repository contains the **Python-based frontend**, built using **Tkinter** as a graphical interface.  
It communicates directly with a **C++ backend server** via **TCP sockets** for secure and efficient messaging.

---

## 🧠 Technologies Used

### 🖥️ Frontend

- **Language:** Python
- **GUI Library:** Tkinter
- **Architecture:**
  - Fully implemented using **Object-Oriented Programming (OOP)**
  - Smooth navigation between screens (e.g., login, topic view, message window)
  - Communication with the server through **TCP sockets**
- **Features:**
  - Register / Log in
  - View and search topics
  - Edit content (only if authorized)
  - Send and receive messages (e.g., authorization requests)
  - update topics
  - check authrizations
  - look up at your own topics

---

## 🔙 Backend (linked project)

- **Language:** C++
- **Libraries Used (installed locally):**
  - `Boost` – `C:\boost_1_87_0`
  - `MySQL Connector/C++` – `C:\mysql-connector-c++`
  - `jsoncpp` – `C:\Users\bardi\Downloads\jsoncpp-master\jsoncpp-master`
- **Architecture:**
  - Asynchronous server with a **thread pool**
  - Designed with **OOP principles**, especially **polymorphism**
  - Communication via **TCP sockets**
- **Security:**
  - All communication encoded/decoded using **ASCII**
  - **Passwords are hashed** before being saved in the database
  - **TCP-only** connections for increased security

---

## 🗄️ Database (MySQL)

- `users` – User credentials and password hashes
- `topics` – Topics and their content
- `messages` – Message log between users (e.g., authorization requests and replies)
- `authorization` – Tracks who can edit which topic

---

## ✨ Summary of Features

- 🧾 Unique topic creation with global visibility
- ✍️ Permission-based editing system
- 👤 User registration and secure authentication
- 🔐 Hashed passwords and ASCII-encoded messaging
- 📩 Internal messaging:
  - Users can **request authorization** to edit a topic
  - Topic owners can **approve or deny** and reply with a message
- 🌐 Secure TCP socket communication
- 🧵 Multithreaded backend (C++) with thread pool
- 🧠 Clean and maintainable OOP design on both client and server
- 🔄 Clear separation of concerns between UI and logic

---

## 🛠️ Build Instructions

1. Open the project folder in **PyCharm**
2. Run `main.py`
3. Make sure the **C++ backend server is running** and listening on the correct TCP port before launching the frontend

---

Feel free to clone and experiment with both sides of the app!  
If you need help with setup or improvements — open an issue or pull request.

