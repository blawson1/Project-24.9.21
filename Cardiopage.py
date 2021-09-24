import tkinter as tk
window = tk.Tk()
window.title("Cardiopage")
# window.geometry("1280x720")


def Cardio_Select():
    Cardio_Select = tk.Frame(master=window)
    Cardio_Select.grid(row=0, column=0)
    Cardio_Select = tk.Label(master=Cardio_Select, text="Select a cardio activity", fg="blue", width=30, height=5)
    Cardio_Select.pack(padx=10, pady=10)

def Run():
    Run = tk.Frame(master=window)
    Run.grid(row=1, column=0)
    Run = tk.Button(master=Run, text="Run", width=30, height=5, command=Running_page)
    Run.pack(padx=10, pady=10)

def Bike():
    Bike = tk.Frame(master=window)
    Bike.grid(row=1, column=1)
    Bike = tk.Button(master=Bike, text="Bike", width=30, height=5, command=Bike_page)
    Bike.pack(padx=10, pady=10)

def Walk():
    Walk = tk.Frame(master=window)
    Walk.grid(row=1, column=2)
    Walk = tk.Button(master=Walk, text="Walk", width=30, height=5, command=Walk_page)
    Walk.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu

def Running_page():
    window.destroy()
    import Runningpage

def Bike_page():
    window.destroy()
    import Bikepage

def Walk_page():
    window.destroy()
    import Walkpage

Cardio_Select()
Bike()
Walk()
Run()
Back()
window.mainloop()
