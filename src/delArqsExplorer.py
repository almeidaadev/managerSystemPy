from os import system as sys
from getUser import *
from platform import system as platform


USER = getlogin()
SYSTEM = platform()

def delArqsExplorer():
  layoutArqs = [
    'Downloads',
    'Documents'
  ]

  cont = 1
  for layout in layoutArqs:
    print(f'{cont} - {layout}')
    cont += 1

  option = int(input('Informe a opção que deseja utilizar: '))
  
  routesArqs = [
    f"C:\\Users\\{USER}\\Downloads",
    f"C:\\Users\\{USER}\\Documents"
  ]

  delArq = [
    f'del /Q /S /F {routesArqs[0]}',
    f'del /Q /S /F {routesArqs[1]}'
  ]
  
  delArqLinux = [
    f'rm -R {routesArqs[0]}',
    f'rm -R {routesArqs[1]}'
  ]

  if SYSTEM == 'Windows':
    match option:
      case 1:
        sys(delArq[0])

      case 2:
        sys(delArq[1])
  
  else:
    match option:
      case 1:
        sys(delArqLinux[0])

      case 2:
        sys(delArqLinux[1])
