def layout(msg):

  options = [
    'Limpar Arquivos Temporarios',
    'Limpar Disco',
    'Limpar Pastas'
    'Sair'
  ]

  print('--' * 30)
  print(msg.center(55))
  print('--' * 30)

  count = 1
  for option in options:
    print(f'{count} - {option}')
    count += 1

  print('--' * 30)
