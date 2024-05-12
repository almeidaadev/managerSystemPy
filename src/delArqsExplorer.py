from os import system as sys
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
  user = str(input('Informe o user do seu computador: '))
  routesArqs = [
    f"C:\\Users\\{user}\\Downloads",
    f"C:\\Users\\{user}\\Documents"
  ]
  delArq = [
    f'del /Q /S /F {routesArqs[0]}',
    f'del /Q /S /F {routesArqs[1]}'
  ]

  match option:
    case 1:
      sys(delArq[0])
    case 2:
      sys(delArq[1])