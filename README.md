# Fernet Encryption Tool

##  About
This project is a **GUI-based encryption and decryption tool** built using **Python, Tkinter, and MySQL**. It utilizes **Fernet encryption** to securely encode and decode messages. The encrypted data is stored in a **MySQL database** for later retrieval.

##  Features
-  Generate encryption keys
-  Encrypt messages securely
-  Decrypt messages using stored keys
-  Save encrypted data to MySQL
-  User-friendly Tkinter GUI

##  Technologies Used
- **Python** (Programming Language)
- **Tkinter** (Graphical User Interface)
- **MySQL** (Database Management System)
- **Cryptography** (Fernet Encryption Library)

##  Installation & Setup
### 1️ Clone the Repository
```sh
git clone https://github.com/your-username/fernet-encryption-tool.git
cd fernet-encryption-tool
```

### 2️ Install Dependencies
Make sure you have Python installed (preferably **Python 3.10+**). Then, install the required dependencies:
```sh
pip install -r requirements.txt
```

### 3️ Setup MySQL Database
Create a MySQL database and a table using the following SQL command:
```sql
CREATE DATABASE fernetencryption;
USE fernetencryption;
CREATE TABLE fernetdata (
    message TEXT,
    encrypted_message TEXT
);
```



### 5️ Run the Application
Execute the script:
```sh
python main.py
```

##  License
This project is open-source .


---
 THANK YOU!!!!!!

