def layout(msg):

  options = [
    # 'Fazer Limpeza Profunda (Todas opções)'
    'Limpar Arquivos Temporarios',
    'Limpar Disco',
    'Limpar Pastas',
    'Esvaziar Lixeira',
    'Ver IPv4',
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