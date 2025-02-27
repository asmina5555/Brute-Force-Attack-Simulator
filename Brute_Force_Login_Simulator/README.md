Brute Force Attack Simulator

- The Brute Force Attack Simulator is a Python-based tool designed to simulate brute force attacks on a login system. 
- It demonstrates how brute force attacks work, the vulnerabilities they exploit, and the countermeasures needed to prevent them. 
- The project includes a Tkinter-based GUI for user interaction, a SQLite database for storing user credentials, and a logging system to track login attempts.

Features

- Brute Force Algorithm: Simulates brute force attacks by generating and testing password combinations.
- Account Lockout Mechanism: Locks user accounts after multiple failed login attempts.
- Password Hashing: Uses the bcrypt library to securely hash and store passwords.
- Logging System: Records all login attempts in a log file (login_attempts.log).
- User-Friendly GUI: Provides an intuitive interface for entering credentials and viewing results.

Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.x: Download and install Python from python.org.
- Required Libraries: Install the required Python libraries using pip:
pip install bcrypt



