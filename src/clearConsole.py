from os import system as sys; import platform

def clearConsole(system = platform.system()):
  if system == 'Windows': return  sys('cls')
  return sys('clear')
