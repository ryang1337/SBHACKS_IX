import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello, world!")
button = tk.Button(root, text="Click me!")

label.pack()
button.pack()
root.mainloop()
