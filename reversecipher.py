import tkinter as tk
from tkinter import messagebox, Label, Text, Button, END, INSERT, RIGHT
import mysql.connector
from cryptography.fernet import Fernet

class FernetGUI:
    def __init__(self, root):
        """
        Initializes the main GUI window and sets up the widgets.
        """
        self.root = root
        self.root.title("FERNET ENCRYPTION AND DECRYPTION")
        self.create_widgets()
    
    def dbconnect(self):
        """
        Establishes a connection to the MySQL database.
        I hsed placeholders with actual database credentials for security, u can use your own if you want to use this code.
        """
        return mysql.connector.connect(host='DB_HOST', database='DB_NAME', user='DB_USER', password='DB_PASSWORD')
    
    def generate_key(self):
        """
        Generates a new Fernet encryption key and displays it in the text box.
        """
        key = Fernet.generate_key()
        self.prik.delete("1.0", "end")  # Clear existing text
        self.prik.insert(INSERT, key.decode())  # Insert the generated key
    
    def encrypt(self):
        """
        Encrypts the user input message using the provided Fernet key and saves it in the database.
        """
        key = self.prik.get("1.0", "end-1c")  # Get the encryption key
        message = self.msg.get("1.0", "end-1c")  # Get the message to encrypt
        
        if not key:
            messagebox.showerror("Error", "Generate Key first")
        elif not message:
            messagebox.showerror("Error", "Type Message first")
        else:
            f = Fernet(key.encode())  # Create Fernet cipher instance
            token = f.encrypt(message.encode())  # Encrypt the message
            
            # Display the encrypted message
            self.cypmsg1.delete("1.0", END)
            self.cypmsg1.insert(INSERT, token.decode())

            # Save to the database
            connection = self.dbconnect()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO fernetdata VALUES (%s, %s)", (message, token.decode()))
            connection.commit()
            cursor.close()
            connection.close()
            
            messagebox.showinfo("Success", "Message successfully encrypted")
    
    def decrypt(self):
        """
        Decrypts the encrypted message using the provided key.
        """
        key = self.prik.get("1.0", "end-1c")  # Get the decryption key
        cyp = self.cypmsg1.get("1.0", "end-1c")  # Get the encrypted message
        
        if not key:
            messagebox.showerror("Error", "There is no key")
        elif not cyp:
            messagebox.showerror("Error", "There is no cipher to decrypt")
        else:
            try:
                f = Fernet(key.encode())  # Create Fernet cipher instance
                decrypted_message = f.decrypt(cyp.encode()).decode()  # Decrypt the message
                
                # Display the decrypted message
                self.cypmsg1.delete("1.0", END)
                self.cypmsg1.insert(INSERT, decrypted_message)
                
                messagebox.showinfo("Success", "Cipher successfully decrypted")
            except:
                messagebox.showerror("Error", "Error in decrypting!")
    
    def create_widgets(self):
        """
        Creates and arranges all the GUI elements (labels, text boxes, buttons).
        """
        Label(self.root, justify=RIGHT, text="FERNET ENCRYPTION IMPLEMENTATION", fg="#ffffff", bg="#007acc",
              width=80, height=1, font=('times', 15, 'bold')).place(x=50, y=10)
        
        # Input field for the encryption key
        Label(self.root, height=1, width=20, text="Fernet Key", fg="white", bg="#005f99", font=('times', 15)).place(x=10, y=70)
        self.prik = Text(self.root, height=2, width=60, bg="white", fg="black")
        self.prik.place(x=300, y=70)
        
        # Input field for the message to be encrypted
        Label(self.root, height=1, width=20, text="Enter Message", fg="white", bg="#005f99", font=('times', 15)).place(x=10, y=170)
        self.msg = Text(self.root, height=5, width=60, bg="white", fg="black")
        self.msg.place(x=300, y=170)
        
        # Output field for encrypted/decrypted message
        Label(self.root, height=1, width=20, text="Cipher", fg="white", bg="#005f99", font=('times', 15)).place(x=10, y=300)
        self.cypmsg1 = Text(self.root, height=5, width=60, bg="white", fg="black")
        self.cypmsg1.place(x=300, y=300)
        
        # Buttons for generating key, encrypting, and decrypting messages
        Button(self.root, text="Generate Key", width=20, fg='#ffffff', bg='#007acc', command=self.generate_key).place(x=800, y=70)
        Button(self.root, text="Encrypt Message", width=20, fg='#ffffff', bg='#007acc', command=self.encrypt).place(x=400, y=270)
        Button(self.root, text="Decrypt Message", width=20, fg='#ffffff', bg='#007acc', command=self.decrypt).place(x=600, y=270)
        
        # Set the window size and start the GUI loop
        self.root.geometry('1000x450')
        self.root.mainloop()

# Main execution: Create and run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = FernetGUI(root)
