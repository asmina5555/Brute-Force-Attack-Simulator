import sqlite3
import bcrypt

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
''')

# Hash password before storing
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

hashed_password = hash_password("123456")  # Securely hashed password

# Insert a dummy user
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", hashed_password))

conn.commit()
conn.close()

print("Database setup completed. User 'admin' created with hashed password.")