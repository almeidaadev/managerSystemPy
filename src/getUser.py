import socket
from os import getlogin

def ver_ipv4():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address
    except socket.error as e:
        print(f"Erro ao obter endereço IPv4: {e}")
        return None

"""
ipv4 = ver_ipv4()
if ipv4:
    print(f"Endereço IPv4: {ipv4}")
else:
    print("Não foi possível obter o endereço IPv4.")

username = user_computer()
print(f"Nome de usuário: {username}")
"""