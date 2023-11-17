import pyautogui
import platform
import ctypes
import subprocess


def detect_os():
    print('\nIdentificando tu sistema operativo...')
    system_platform = platform.system()
    if system_platform == "Windows":
        # Prevent sleep on Windows
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    elif system_platform == "Darwin":
        # Prevent sleep on Mac
        subprocess.run(["caffeinate", "-u", "-t", "1"])
        system_platform = 'MacOS'
    print(f'\nSistema operativo detectado:  {system_platform}')

def click(intervalo):
    wh = pyautogui.size()
    width = wh[0]/4
    height = (wh[1]/2) * -1
    pyautogui.move(width, height)

    pyautogui.click(width, height, button='left',interval=intervalo)




def main():
    intervalo = input('Cada cuanto quieres que haga click?>> ')
    detect_os()
    click(intervalo)

if __name__ == '__main__':
    main()