# dionaea
a fake SSH honeypot written in Python that simulates a Linux login shell over TCP/Telnet. This beginner tool is designed for analysts and researchers to simulate monitoring and logging unauthorized access attempts in a safe, controlled environment.

---

## Features

- Simulates a basic SSH login prompt (`SSH-2.0-OpenSSH_7.6p1`)
- Accepts any username/password and logs them
- Provides a fake Linux shell with basic commands:
  - `ls`, `whoami`, `pwd`, `exit`
- Supports backspace during input (realistic interaction)
- Logs:
  - IP address
  - Login credentials
  - Commands issued
- Clean line formatting for smooth Telnet sessions

---

## Technologies

- Python
- Socket API (raw TCP)
- Telnet-compatible interface

---

## Project Structure
dionaea/
├── dionaea.py # Main honeypot logic
├── logger.py # Centralized logging utility
├── logs/
│ └── activity.log # All connection activity
└── README.md

