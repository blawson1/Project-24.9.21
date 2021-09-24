import tkinter as tk

window = tk.Tk()
window.title("Legspage")
# window.geometry("1280x720")

def Legs_Select():
    Legs_Select = tk.Frame(master=window)
    Legs_Select.grid(row=0, column=0)
    Legs_Select = tk.Label(master=Legs_Select, text="Select a legs workout", fg="blue", width=30, height=5)
    Legs_Select.pack(padx=10, pady=10)

def Squats():
    Squats = tk.Frame(master=window)
    Squats.grid(row=1, column=0)
    Squats = tk.Button(master=Squats, text="Squats", width=30, height=5)
    Squats.pack(padx=10, pady=10)

def Step_ups():
    Step_ups = tk.Frame(master=window)
    Step_ups.grid(row=1, column=1)
    Step_ups = tk.Button(master=Step_ups, text="Step ups", width=30, height=5)
    Step_ups.pack(padx=10, pady=10)

def Lunges():
    Lunges = tk.Frame(master=window)
    Lunges.grid(row=1, column=2)
    Lunges = tk.Button(master=Lunges, text="Lunges", width=30, height=5)
    Lunges.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu


Legs_Select()
Squats()
Step_ups()
Lunges()
Back()
window.mainloop()
