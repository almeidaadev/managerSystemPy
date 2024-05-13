OPTIONS = [
  'Limpar Arquivos Temporários',
  'Limpar Pastas', 
  'Esvaziar Lixeira',
  'Limpar Disco',
  'Ver IPv4',
  'Sair'
  ]

def layoutConsole(msg):
  print("--" * 30)
  print(msg.center(60))
  print("--" * 30)

  cont = 1
  for i in OPTIONS:
    print(f'{cont} - {i}')
    cont += 1 

  print("--" * 30)

#layoutConsole('Manager System')