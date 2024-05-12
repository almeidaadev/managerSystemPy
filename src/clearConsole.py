from os import system as sys;
import platform

def clearConsole(systemOperation = platform.system()):
  if systemOperation == 'Windows': return sys('cls')
  return sys('clear')