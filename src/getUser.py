import socket
from os import getlogin

def ver_ipv4():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except socket.error as e:
        print(f"Erro ao obter endereço IPv4: {e}")
        return