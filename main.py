import tkinter as tk
from tkinter import ttk
import engine
#import realtime

# root window
root = tk.Tk()
root.geometry('700x400')
root.resizable(False, False)
root.title('Button Demo')

# scan files
exit_button = ttk.Button(
    root,
    text='scan for virus ',

    command=lambda: print(engine.virusscanner("C:\\Users\\suhan\\Desktop\\test")) #put your file location here
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


# remove virus
exit1_button = ttk.Button(
    root,
    text='remove the virus',
    command=lambda: print(engine.virusremover("C:\\Users\\suhan\\Desktop\\test")) #put your file location here
)

exit1_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#junk file remover
exit1_button = ttk.Button(
    root,
    text='remove junk files',
    command=lambda: print(engine.junkfileremover())
)

exit1_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#ram health manager
exit1_button = ttk.Button(
    root,
    text='manage ram health',
    command=lambda: print(engine.rambooster())
)

exit1_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#real time protector
#exit1_button = ttk.Button(
    #root,
    #text='realtime protector',
    #command=lambda: print(realtime.RealTime())
#)

#exit1_button.pack(
    #ipadx=5,
    #ipady=5,
    #expand=True
#)



root.mainloop()
