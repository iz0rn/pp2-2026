import tkinter as tk

window = tk.Tk()
window.title("Hello 김민재")
window.geometry("400x200")

label = tk.Label(window, text="Hello tkinter")
label.pack()

window.mainloop()