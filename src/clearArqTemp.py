from os import system as sys
from getUser import *
def clearArqTemps():
  user = getlogin()
  routes = [
    'C:\\Windows\\Temp',
    f'C:\\Users\\{user}\\AppData\\Local\\Temp',
    'C:\\Windows\\prefetch'
  ]

  for delRoutes in routes:
    cmdDel = f'del /Q /S /F {delRoutes}'
    sys(cmdDel)