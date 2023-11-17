import pyautogui
import os
import time
import platform
from datetime import datetime

def detect_os():
    print('\nIdentificando tu sistema operativo...')
    system_platform = platform.system()
    if system_platform == "Windows":
        # Prevent sleep on Windows
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    elif system_platform == "Darwin":
        # Prevent sleep on Mac
        import subprocess
        subprocess.run(["caffeinate", "-u", "-t", "1"])
        system_platform = 'MacOS'
    print(f'\nSistema operativo detectado:  {system_platform}\n')

def click(intervalo):
    intervalo = int(intervalo)
    width = 1032
    height = 26
    contador = 0
    while True:
        pyautogui.click(width, height, button='left')
        
        contador+=1
        tiempo = (contador * intervalo)/60
        temp = f"{tiempo:.2f}"

        print(f"\rClick: {contador} > Tiempo ejecutando: {temp}", end='', flush=True) 

        time.sleep(int(intervalo))





def main():
    intervalo = input('Cada cuanto quieres que haga click?>> ')
    detect_os()
    click(intervalo)

if __name__ == '__main__':
    main()