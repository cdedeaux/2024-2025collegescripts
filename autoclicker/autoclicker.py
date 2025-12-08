import pyautogui
import time
import threading
from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Auto Clicker")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Label(mainframe, text="Auto Clicker").grid(column=1, row=1, columnspan=3)

clicking = False

def start_clicking():

    while clicking:
        delay = 0.1  # Delay in seconds between clicks
        pyautogui.click() # Default is left click
        time.sleep(delay)


def on_start():
    global clicking
    clicking = True
    threading.Thread(target=start_clicking).start()
def on_stop():
    global clicking
    clicking = False
    pass  # Implement stop functionality if needed
ttk.Button(mainframe, text="Start", command=on_start).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Stop", command=on_stop).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.quit).grid(column=3, row=3, sticky=W)
root.mainloop()