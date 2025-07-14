import socket
from responses import get_response
from logger import setup_logger

logger = setup_logger()

FAKE_RESPONSES = {
    "ls": "Documents  Downloads  Music  Pictures",
    "whoami": "root",
    "pwd": "/root"
}

def clean_input(s):
    buffer = []
    for char in s:
        if char in ('\x08', '\x7f'):  # Handle backspace/delete
            if buffer:
                buffer.pop()
        else:
            buffer.append(char)
    return ''.join(buffer)

def simulate_shell(conn, ip):
    try:
        sock_file = conn.makefile('rwb', buffering=0)

        # Fake login
        conn.sendall(b"\r\nlogin: ")
        raw_username = sock_file.readline().decode(errors="ignore").strip()
        username = clean_input(raw_username)

        conn.sendall(b"Password: ")
        raw_password = sock_file.readline().decode(errors="ignore").strip()
        password = clean_input(raw_password)

        logger.info(f"{ip} attempted login with username='{username}' password='{password}'")

        # Fake shell banner
        conn.sendall(b"\r\nAccess granted.\r\n")
        conn.sendall(b"Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-75-generic x86_64)\r\n\r\n")

        for _ in range(3):
            conn.sendall(b"root@dionaea:~# ")
            raw_command = sock_file.readline().decode(errors="ignore").strip()
            command = clean_input(raw_command).lower()

            if not command:
                continue

            logger.info(f"{ip} ran command: {command}")

            if command == "exit":
                conn.sendall(b"logout\r\n")
                break

            response = get_response(command)
            if not response.endswith("\r\n"):
                response += "\r\n"
            conn.sendall(response.encode())


        conn.sendall(b"\r\nSession closed.\r\n")
    except Exception as e:
        logger.warning(f"Session error with {ip}: {e}")
    finally:
        conn.close()

def start_honeypot(host='0.0.0.0', port=2222):
    logger.info(f"Starting dionaea on {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)

        while True:
            conn, addr = server_socket.accept()
            ip, port = addr
            logger.info(f"Connection from {ip}:{port}")
            conn.sendall(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4\r\n")
            simulate_shell(conn, ip)

if __name__ == '__main__':
    start_honeypot()
