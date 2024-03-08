import tkinter as tk
import sqlite3
# Predefined usernames and passwords
doctor_username = "doctor"
doctor_password = "password"
client_username = "client"
client_password = "password"

def select_age():
    # Retrieve the selected option
    selected_age = age_var.get()
    
    # Show login form for doctor or client based on the selection
    if selected_age == "Doctor":
        show_doctor_login()
    elif selected_age == "Client":
        show_client_login()

def show_doctor_login():
    # Hide the age selection frame
    age_frame.pack_forget()
    
    # Show the doctor login frame
    doctor_login_frame.pack()

def show_client_login():
    # Hide the age selection frame
    age_frame.pack_forget()
    
    # Show the client login frame
    client_login_frame.pack()

def doctor_login():
    username = doctor_username_entry.get()
    password = doctor_password_entry.get()
    
    # Simple validation
    if username == doctor_username and password == doctor_password:
        result_label.config(text="Doctor login successful")
        # Call the function to show the doctor menu
        show_doctor_login()
    else:
        result_label.config(text="Doctor login failed")

    # Simple validation
    if username == doctor_username and password == doctor_password:
        result_label.config(text="Doctor login successful")
        open_menu()
    else:
        result_label.config(text="Doctor login failed")

def client_login():
    # Retrieve username and password entered by the user
    username = client_username_entry.get()
    password = client_password_entry.get()
    
    # Simple validation
    if username == client_username and password == client_password:
        result_label.config(text="Client login successful")
        open_menu()
    else:
        result_label.config(text="Client login failed")

def open_menu():
    # Close the login window
    root.withdraw()
    
    # Create a new window for the menu
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    
    # Create and place widgets for the menu
    menu_label = tk.Label(menu_window, text="Welcome to the Menu!")
    menu_label.pack(padx=10, pady=5)
    
    # You can add more widgets and functionality to the menu as needed

# Create the main window
root = tk.Tk()
root.title("Age Selection")

# Create a frame for age selection
age_frame = tk.Frame(root)
age_frame.pack()

age_label = tk.Label(age_frame, text="Select Your Role:")
age_label.grid(row=0, column=0, padx=10, pady=5)

age_var = tk.StringVar()
age_var.set("Doctor")  # Default selection
age_option_menu = tk.OptionMenu(age_frame, age_var, "Doctor", "Client")
age_option_menu.grid(row=0, column=1, padx=10, pady=5)

age_select_button = tk.Button(age_frame, text="Select", command=select_age)
age_select_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Create frames for doctor login and client login
doctor_login_frame = tk.Frame(root)
client_login_frame = tk.Frame(root)

# Widgets for doctor login
doctor_username_label = tk.Label(doctor_login_frame, text="Username:")
doctor_username_label.grid(row=0, column=0, padx=10, pady=5)

doctor_username_entry = tk.Entry(doctor_login_frame)
doctor_username_entry.grid(row=0, column=1, padx=10, pady=5)

doctor_password_label = tk.Label(doctor_login_frame, text="Password:")
doctor_password_label.grid(row=1, column=0, padx=10, pady=5)

doctor_password_entry = tk.Entry(doctor_login_frame, show="*")
doctor_password_entry.grid(row=1, column=1, padx=10, pady=5)

doctor_login_button = tk.Button(doctor_login_frame, text="Login", command=doctor_login)
doctor_login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Widgets for client login
client_username_label = tk.Label(client_login_frame, text="Username:")
client_username_label.grid(row=0, column=0, padx=10, pady=5)

client_username_entry = tk.Entry(client_login_frame)
client_username_entry.grid(row=0, column=1, padx=10, pady=5)

client_password_label = tk.Label(client_login_frame, text="Password:")
client_password_label.grid(row=1, column=0, padx=10, pady=5)

client_password_entry = tk.Entry(client_login_frame, show="*")
client_password_entry.grid(row=1, column=1, padx=10, pady=5)

client_login_button = tk.Button(client_login_frame, text="Login", command=client_login)
client_login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

def init_db():
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    
    # Create a table for doctors
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL)''')
    
    # Create a table for patients
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL,
                      doctor_id INTEGER,
                      family_id INTEGER,
                      FOREIGN KEY(doctor_id) REFERENCES doctors(id),
                      FOREIGN KEY(family_id) REFERENCES family_groups(id))''')
    
    # Create a table for family groups
    cursor.execute('''CREATE TABLE IF NOT EXISTS family_groups (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL UNIQUE)''')
    
    # Create a table for patient logs
    cursor.execute('''CREATE TABLE IF NOT EXISTS patient_logs (
                      id INTEGER PRIMARY KEY,
                      patient_id INTEGER NOT NULL,
                      date TEXT NOT NULL,
                      log TEXT NOT NULL,
                      FOREIGN KEY(patient_id) REFERENCES patients(id))''')
    
    # Create a table for referrals
    cursor.execute('''CREATE TABLE IF NOT EXISTS referrals (
                      id INTEGER PRIMARY KEY,
                      patient_id INTEGER NOT NULL,
                      specialist TEXT NOT NULL,
                      reason TEXT NOT NULL,
                      date TEXT NOT NULL,
                      FOREIGN KEY(patient_id) REFERENCES patients(id))''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the init_db function to initialize the database
init_db()
def fetch_families_from_db():
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name FROM family_groups")
    families = cursor.fetchall()
    
    conn.close()
    return families

def show_doctor_menu():
    doctor_menu_window = tk.Toplevel(root)
    doctor_menu_window.title("Doctor Menu")

    # Button to view family groups
    view_families_button = tk.Button(doctor_menu_window, text="View Family Groups", command=view_family_groups)
    view_families_button.pack(padx=10, pady=5)

    # Button to manage referrals
    manage_referrals_button = tk.Button(doctor_menu_window, text="Manage Referrals", command=manage_referrals)
    manage_referrals_button.pack(padx=10, pady=5)

def view_family_groups():
    family_window = tk.Toplevel(root)
    family_window.title("Family Groups")
    
    families = fetch_families_from_db()
    for family_id, name in families:
        tk.Button(family_window, text=name, command=lambda fid=family_id: view_family_members(fid)).pack(padx=10, pady=5)

    
    # Here you would fetch family groups from the database and create a list or another suitable UI component
    # to display them. For simplicity, this is not fully implemented here.
    # Example:
    # families = fetch_families_from_db()
    # for family in families:
    #     tk.Button(family_window, text=family["name"], command=lambda f=family: view_family_members(f["id"])).pack()
def view_family_members(family_id):
    members_window = tk.Toplevel(root)
    members_window.title("Family Members")
    
    # Fetch family members from the database using family_id and display them
    # When a member is selected, provide an option to view/edit logs
def manage_referrals():
    referrals_window = tk.Toplevel(root)
    referrals_window.title("Manage Referrals")
    
    # Here you would implement functionality to add new referrals and view existing ones.
    # This could include forms to input new referrals and a list or table to display them.