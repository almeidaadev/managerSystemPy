from os import system as sys
from getUser import *
from platform import system as platform


SYSTEM = platform()
USER = getlogin()

def clearArqTemps():
  ROUTES = [
    'C:\\Windows\\Temp',
    f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
    'C:\\Windows\\prefetch'
  ]

  if SYSTEM == 'Windows':
    for delRoutes in ROUTES:
      cmdDel = f'del /Q /S /F {delRoutes}'
      sys(cmdDel)
  
  else:
    for delRoutes in ROUTES:
      cmdDel = f'rm -RF {delRoutes}'
      sys(cmdDel)