from platform import system as platform
from os import system as sys
import os

SYSTEM = platform()

def esvaziarLixeira():
  path = 'C:\\$Recycle.Bin'

  home_dir = os.path.expanduser("~")
  trash_path = os.path.join(home_dir, ".local/share/Trash")

  if SYSTEM == 'Windows':
    return sys(f'del /Q /S /F {path}')
  return sys(f'rm -R {trash_path}')