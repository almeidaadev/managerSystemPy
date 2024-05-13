from time import sleep
from delArqsExplorer import delArqsExplorer
from layoutWindow import layoutWindow
from clearConsole import clearConsole
from clearArqTemp import clearArqTemps
from cleanDisk import cleanDisk
from esvaziarLixeira import esvaziarLixeira
from getUser import ver_ipv4
from layoutConsole import layoutConsole
from layoutWindow import layout
def callFuntion():
  sleep(1)
  clearConsole()
  layoutWindow('Manager System')
  #layoutConsole('Manager System')
  optionUser()

def optionUser():
  user = str(input('Deseja utilizar qual opção: '))

  try:
    if user != '' and user.isnumeric() and int(user) > 0 and int(user) < 7:
      user = int(user)

      match user:
        case 1:
          clearArqTemps()
          callFuntion()
          
        case 2:
          cleanDisk()
          callFuntion()
          
        case 3:
          delArqsExplorer()
          callFuntion()

        case 4:
          esvaziarLixeira()
          callFuntion()

        case 5:
          ver_ipv4()
          user = input('Aperte qualquer tecla pra continuar: ')
          callFuntion()

        case 6:
          exit()

    else:
      print('Digite um numero valido')
      callFuntion()
      
  except ValueError:
    print(f'{ValueError} - Informe um valor numerico valido')
    callFuntion()