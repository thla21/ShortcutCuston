import pyautogui
import keyboard
import time

# Etapa 1 = Criar a função desejada
def task():
    time.sleep(1)
    # Abrir o navegador
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)
    # Entrar no google meet para reunião
    pyautogui.write("https://meet.google.com")
    pyautogui.press("enter")
    time.sleep(3)
    # Entrar na sala de reunião
    pyautogui.press("enter")
    
# Associar a função craida au uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+f", task)

keyboard.wait("esc")
