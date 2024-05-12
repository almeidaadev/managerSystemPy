from os import system as sys
from platform import system as platform

SYSTEM = platform()

def esvaziarLixeira():
  path = 'C:\\$Recycle.Bin'
  if SYSTEM == 'Windows':
    return sys(f'del /Q /S /F {path}')
  return sys(f'rm -RF {path}')