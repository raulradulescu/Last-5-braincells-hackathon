import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import db

class GPConnectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GP Patient Connector")
        self.root.geometry('400x300')
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=20)
        
        self.show_login_screen()
    def show_login_screen(self):
        # Clear previous frame content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Add login widgets
        ttk.Label(self.main_frame, text="Login", font=('Arial', 16)).pack(pady=10)
        # Username
        username_label = ttk.Label(self.main_frame, text="Username")
        username_label.pack()
        self.username_entry = ttk.Entry(self.main_frame)
        self.username_entry.pack()
        # Password
        password_label = ttk.Label(self.main_frame, text="Password")
        password_label.pack()
        self.password_entry = ttk.Entry(self.main_frame, show="*")
        self.password_entry.pack()
        # Login Button
        login_button = ttk.Button(self.main_frame, text="Login", command=self.login)
        login_button.pack(pady=10)
        # Register Button
        register_button = ttk.Button(self.main_frame, text="Register", command=self.show_register_screen)
        register_button.pack()

    def login(self):
        # Implement login functionality
        pass

    def show_register_screen(self):
        # Clear previous frame content and show registration widgets
        pass

def main():
    root = tk.Tk()
    app = GPConnectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()