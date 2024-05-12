from os import system as sys;
from platform import system as platform

def clearConsole(systemOperation = platform()):
  if systemOperation == 'Windows': return sys('cls')
  return sys('clear')