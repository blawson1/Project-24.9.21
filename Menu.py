import tkinter as tk
window = tk.Tk()
window.title("Menu")
# window.geometry("1280x720")

for i in range(0, 3):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)

def Option_Select():
    Option_Select = tk.Frame(master=window)
    Option_Select.grid(row=0, column=0)
    Option_Select = tk.Label(master=Option_Select, text="Select an option", fg="blue", width=30, height=5)
    Option_Select.pack(padx=10, pady=10)

def Exit():
    Exit = tk.Frame(master=window)
    Exit.grid(row=3, column=1)
    Exit = tk.Button(master=Exit, text="Exit", width=30, height=5, bg="yellow", fg="red", command=quit)
    Exit.pack(padx=10, pady=10)

def Cardio():
    Cardio = tk.Frame(master=window)
    Cardio.grid(row=1, column=0)
    Cardio = tk.Button(master=Cardio, text="Cardio", width=30, height=5, command=Cardio_page)
    Cardio.pack(padx=10, pady=10)

def Arms():
    Arms = tk.Frame(master=window)
    Arms.grid(row=1, column=1)
    Arms = tk.Button(master=Arms, text="Arms/Upper Body", width=30, height=5, command=Arms_page)
    Arms.pack(padx=10, pady=10)

def Legs():
    Legs = tk.Frame(master=window)
    Legs.grid(row=2, column=0)
    Legs = tk.Button(master=Legs, text="Legs/Lower Body", width=30, height=5, command=Legs_page)
    Legs.pack(padx=10, pady=10)

def Core():
    Core = tk.Frame(master=window)
    Core.grid(row=2, column=1)
    Core = tk.Button(master=Core, text="Core", width=30, height=5, command=Core_page)
    Core.pack(padx=10, pady=10)

def Settings():
    Core = tk.Frame(master=window)
    Core.grid(row=3, column=0)
    Core = tk.Button(master=Core, text="Settings", bg="light blue", width=30, height=5, command=Settings_page)
    Core.pack(padx=10, pady=10)

def Cardio_page():
    window.destroy()
    import Cardiopage

def Arms_page():
    window.destroy()
    import Armspage

def Legs_page():
    window.destroy()
    import Legspage

def Core_page():
    window.destroy()
    import Legspage

def Settings_page():
    window.destroy()
    import SETTINGS

Option_Select()
Exit()
Cardio()
Arms()
Legs()
Core()
Settings()
window.mainloop()
# or just mainloop() but something .mainloop lets you do many mainloops if you wanted to
