from os import system as sys
from getUser import *
from platform import system as platform

SYSTEM = platform()
USER = getlogin()

ROUTES_WINDOWS = [
  'C:\\Windows\\Temp',
  f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
  'C:\\Windows\\prefetch'
]

ROUTES_LINUX = [
  'C:\\Windows\\Temp',
  f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
  'C:\\Windows\\prefetch'
]

def clearArqTemps():
  if SYSTEM == 'Windows':
    for delRoutes in ROUTES_WINDOWS:
      cmdDel = f'del /Q /S /F {delRoutes}'
      return sys(cmdDel)