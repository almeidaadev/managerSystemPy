# from pathlib import Path

# users = [
#   x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()
# ]
# print(users)

import socket
from os import getlogin

def andressLocalHost():
  print(f"Esses São seus IPs: \n{"\n".join(socket.gethostbyname_ex(socket.gethostname())[-1])}")

def userComputer():
  return getlogin()
