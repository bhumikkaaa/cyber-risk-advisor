import socket
import re

def check_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex(('127.0.0.1', port))
        s.close()

        if result == 0:
            return f"Port {port} Open"
    except:
        pass
    return None


def check_password(password):
    if len(password) < 8:
        return "Weak Password (Too short)"
    if not re.search("[A-Z]", password):
        return "Weak Password (No uppercase)"
    if not re.search("[0-9]", password):
        return "Weak Password (No number)"
    return None
