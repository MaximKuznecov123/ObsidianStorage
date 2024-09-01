from pyperclip import paste
from datetime import datetime as dt

with open("C:\\Users\\User\\Desktop\\ObsidianStorage\\VERYBIGtoSee.md", "a", encoding="utf-8") as file:
    import pyautogui as pag
    pag.hotkey("ctrl", "c")
    text = paste().replace('\r\n', '\n')
    file.write((f"~~~ {dt.now()}\n" + \
                f"{text}\n" + \
                "~~~\n\n"))