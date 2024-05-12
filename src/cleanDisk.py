from os import system as sys
from platform import system as platform

SYSTEM = platform()

def Disk():
  sys('cleanmgr/sagerun')

def cleanDisk():
  if SYSTEM == 'Windows':
    return Disk()
  return print('O sistema operacional possui desfragmentação de disco. ')