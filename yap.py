from tkinter import *

import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()

window.title("Welcome to LikeGeeks app")

window.mainloop()
