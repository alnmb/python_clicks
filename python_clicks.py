import os
import time
import platform
from datetime import datetime
import subprocess
import sys
import atexit

def maximize_window(title):
    import pygetwindow as gw
    window = gw.getWindowsWithTitle(title)
    if window:
        window[0].maximize()

def get_active_window_title():
    import pygetwindow as gw
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    else:
        return None

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

def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining

def click():
    import pyautogui
    intervalo = input('Cada cuanto quieres que haga click?>> ')
    intervalo = int(intervalo)
    width = 1032
    height = 26
    contador = 0

    print('Presione ctrl+c para detener el script')
    try:
        while True:
            pyautogui.click(width, height, button='left')
            
            contador+=1
            calc_tiempo = (contador * intervalo)
            horas,minutos,segundos = convert_time(calc_tiempo)

            print(f"\rClick: {contador} > Tiempo ejecutando: {horas}:{minutos}:{segundos}", end='', flush=True) 

            time.sleep(int(intervalo))
            pass
    
    except KeyboardInterrupt:
         # Handle Ctrl+C (user interruption) gracefully
        print("\nDeteniendo el script")
        #os.system('deactivate')
    # finally:
    #     os.system('deactivate')
    

def main():

    title = get_active_window_title()
    print("Active Window Title:", title)
    maximize_window(title)
    detect_os()
    atexit.register(click)
    

if __name__ == '__main__':
    main()