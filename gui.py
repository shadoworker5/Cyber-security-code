import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import pyttsx3


def alert():
    messagebox.showinfo("Info", "Hello world")

root = tk.Tk()
root.title = "Printer result"
root.geometry("800x600")
# root.configure(bg='#ffffff')
# root.resizable(0, 0)

bot = pyttsx3.init()
voice_var = tk.IntVar()

text_box = ScrolledText(root, font=("Sitka Small", 11), bd=2, relief=tk.GROOVE, wrap=tk.WORD, undo=True)
text_box.place(x=5, y=5, height=270, width=580)

frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.place(x=585, y=5, height=270, width=210)

frame2 = tk.LabelFrame(frame, text="Change speed")
frame2.grid(row=0, column=0, padx=4, pady=5)

speed_scale = tk.Scale(frame2, from_=100, to=300, orient=tk.HORIZONTAL, length=180, bg='#ffffff')
speed_scale.set(200)
speed_scale.grid(row=2, columnspan=1, ipadx=5, ipady=5)

frame3 = tk.LabelFrame(frame, text="Change voice")
frame3.grid(row=1, column=0, pady=5)

R1 = tk.Radiobutton(frame3, text="Male", variable=voice_var, value=1)
R1.grid(row=0, column=0, ipadx=7, ipady=5, padx=5)

R2 = tk.Radiobutton(frame3, text="Female", variable=voice_var, value=0)
R2.grid(row=0, column=1, ipadx=7, ipady=5, padx=5)

frame4 = tk.Frame(frame, bd=2, relief=tk.SUNKEN)
frame4.grid(row=2, column=0, pady=10)

btn_1 = tk.Button(frame4, text="Convert and Play", width=15, command=alert)
btn_1.grid(row=0, column=0, ipady=5, padx=4, pady=5)

btn_2 = tk.Button(frame4, text="Save as audio", width=15)
btn_2.grid(row=1, column=0, ipady=5, padx=4, pady=5)

btn_3 = tk.Button(frame4, text="Clear", width=10)
btn_3.grid(row=0, column=1, ipady=5, padx=4, pady=5)

btn_4 = tk.Button(frame4, text="Exit", width=10, command=exit)
btn_4.grid(row=1, column=1, ipady=5, padx=4, pady=5)



root.mainloop()
