from os import system as sys

def clearArqTemps():
  user = str(input('Informe o user do seu computador: '))
  routes = [
    'C:\\Windows\\Temp',
    f'C:\\Users\\{user}\\AppData\\Local\\Temp',
    'C:\\Windows\\prefetch'
  ]

  for delRoutes in routes:
    cmdDel = f'del /Q /S /F {delRoutes}'
    sys(cmdDel)