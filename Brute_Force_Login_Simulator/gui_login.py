import tkinter as tk
import sqlite3
import bcrypt
import time
import logging

# Configure logging (automatically creates login_attempts.log)
logging.basicConfig(filename="login_attempts.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Track failed login attempts for account lockout
failed_attempts = {}

def login():
    global failed_attempts

    username = user_entry.get()
    password = pass_entry.get()
    
    current_time = time.time()
    
    # Check if the user is locked out
    if username in failed_attempts and failed_attempts[username]["count"] >= 3:
        if current_time - failed_attempts[username]["time"] < 30:  # Lockout period of 30 seconds
            result_label.config(text="Too many failed attempts. Try again later.", fg="red")
            logging.warning(f"Locked login attempt for user '{username}'")
            return
        else:
            failed_attempts[username]["count"] = 0  # Reset after timeout

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode(), user[0].encode()):
        result_label.config(text="Login Successful", fg="green")
        failed_attempts[username] = {"count": 0, "time": current_time}  # Reset failed attempts
        logging.info(f"Successful login for user '{username}'")
    else:
        if username not in failed_attempts:
            failed_attempts[username] = {"count": 0, "time": current_time}
        
        failed_attempts[username]["count"] += 1
        failed_attempts[username]["time"] = current_time

        if failed_attempts[username]["count"] >= 3:
            result_label.config(text="Too many failed attempts. Locked for 30 sec.", fg="red")
            logging.warning(f"User '{username}' locked out after multiple failed attempts.")
        else:
            result_label.config(text=f"Login Failed. Attempts: {failed_attempts[username]['count']}", fg="red")
            logging.warning(f"Failed login attempt {failed_attempts[username]['count']} for user '{username}'")

    conn.close()

# Tkinter GUI
root = tk.Tk()
root.title("Brute Force Login Simulator")

tk.Label(root, text="Username:").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password:").pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=login).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()