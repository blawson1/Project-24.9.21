import tkinter as tk
window = tk.Tk()
window.title("Cardiopage")
# window.geometry("1280x720")


def Delete_Account():
    Delete_Account = tk.Frame(master=window)
    Delete_Account.grid(row=1, column=2)
    Delete_Account = tk.Button(master=Delete_Account, text="Delete Account", fg="red", width=30, height=5, command=Confirmation)
    Delete_Account.pack(padx=10, pady=10)

def Change_account():
    Change_account = tk.Frame(master=window)
    Change_account.grid(row=0, column=2)
    Change_account = tk.Button(master=Change_account, text="Change account details", fg="blue", width=30, height=5, command=Changeaccount)
    Change_account.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=2)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu

def Confirmation():
    window.destroy()
    import Confirmation

def Changeaccount():
    window.destroy()
    import Changeaccountpage

Delete_Account()
Change_account()
Back()
window.mainloop()
