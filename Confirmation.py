import tkinter as tk
window = tk.Tk()
window.title("Cardiopage")
# window.geometry("1280x720")


def Confirmation():
    Confirmation = tk.Frame(master=window)
    Confirmation.grid(row=0, column=0)
    Confirmation = tk.Button(master=Confirmation, text="Are you sure you want \n to delete your account?".upper(), font="Arial", fg="red", width=30, height=5)
    Confirmation.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=0)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu


Confirmation()
Back()
window.mainloop()
