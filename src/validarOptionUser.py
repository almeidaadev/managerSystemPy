from time import sleep
from delArqsExplorer import delArqsExplorer
from layoutConsole import layout
from clearConsole import clearConsole
from clearArqTemp import clearArqTemps
from cleanDisk import cleanDisk

def callFuntion():
  sleep(1)
  clearConsole()
  layout('test')
  optionUser()

def optionUser():
  user = str(input('Deseja utilizar qual opção: '))

  try:
    if user != '' and user.isnumeric() and int(user) > 0 and int(user) < 4:
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
          exit()
    else:
      print('Digite um numero')
      callFuntion()
      
  except ValueError:
    print(f'{ValueError} - Informe um valor numerico valido')
    callFuntion()