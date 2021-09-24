import tkinter as tk

window = tk.Tk()
window.title("Corepage")
# window.geometry("1280x720")

def Core_Select():
    Core_Select = tk.Frame(master=window)
    Core_Select.grid(row=0, column=0)
    Core_Select = tk.Label(master=Core_Select, text="Select a core workout", fg="blue", width=30, height=5)
    Core_Select.pack(padx=10, pady=10)

def Burpees():
    Burpees = tk.Frame(master=window)
    Burpees.grid(row=1, column=0)
    Burpees = tk.Button(master=Burpees, text="Burpees", width=30, height=5)
    Burpees.pack(padx=10, pady=10)

def Sit_ups():
    Sit_ups = tk.Frame(master=window)
    Sit_ups.grid(row=1, column=1)
    Sit_ups = tk.Button(master=Sit_ups, text="Sit ups", width=30, height=5)
    Sit_ups.pack(padx=10, pady=10)

def Plank():
    Plank = tk.Frame(master=window)
    Plank.grid(row=1, column=2)
    Plank = tk.Button(master=Plank, text="Plank", width=30, height=5)
    Plank.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu

Core_Select()
Burpees()
Sit_ups()
Plank()
Back()
window.mainloop()

