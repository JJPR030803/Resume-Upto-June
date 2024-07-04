import subprocess as sb
import pyautogui as pg
import time

notepad_path = r"C:\Windows\System32\notepad.exe"
sb.Popen(notepad_path)
time.sleep(2)
pg.click()
pg.write('Hola Mundo')