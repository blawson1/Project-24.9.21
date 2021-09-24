import sqlite3
import tkinter as tk
window = tk.Tk()
window.title("Main_program")
window.geometry('1280x720')

var = tk.StringVar()
var.set('male')

for i in range(0, 3):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)

# --------------------- Right Frame ----------------
frm_right = tk.Frame(master=window)
frm_right.grid(row=0, column=1)

lbl_register = tk.Label(master=frm_right, text='Change account details', fg='blue', width=60, height=5)
lbl_register.grid(row=0, column=0)

# Name, gender, age, height, weight, email, password
# -------------------- Name Label ----------------
lbl_name = tk.Label(master=frm_right, text='Name: ', fg='black', width=60, height=3)
lbl_name.grid(row=1, column=0)
# -------------------- Name Entry ----------------
ent_new_name = tk.Entry(master=frm_right, fg='black', bg='white',)
ent_new_name.grid(row=1, column=1)
# -------------------- Age Label ----------------
lbl_age = tk.Label(master=frm_right, text='Age: ', fg='black', width=60, height=3)
lbl_age.grid(row=2, column=0)
# -------------------- Age Entry ----------------
ent_age = tk.Entry(master=frm_right, fg='black', bg='white',)
ent_age.grid(row=2, column=1)
# -------------------- Gender Frame ----------------
frm_gender = tk.Frame(master=frm_right)
frm_gender.grid(row=3, column=1, columnspan=2)
# -------------------- Gender Frame Radio Buttons ----------------
male_rb = tk.Radiobutton(frm_gender, text='Male', variable=var, value='male')
female_rb = tk.Radiobutton(frm_gender, text='Female', variable=var, value='female')
others_rb = tk.Radiobutton(frm_gender, text='Other', variable=var, value='others')
male_rb.grid(row=0, column=0)
female_rb.grid(row=0, column=1)
others_rb.grid(row=0, column=2)
# -------------------- Height Label ----------------
lbl_height = tk.Label(master=frm_right, text='Height (cm): ', fg='black', width=60, height=3)
lbl_height.grid(row=4, column=0)
# -------------------- Height Entry ----------------
ent_height = tk.Entry(master=frm_right, fg='black', bg='white',)
ent_height.grid(row=4, column=1)
# -------------------- Weight Label ----------------
lbl_weight = tk.Label(master=frm_right, text='Weight (kg): ', fg='black', width=60, height=3)
lbl_weight.grid(row=5, column=0)
# -------------------- Weight Entry ----------------
ent_weight = tk.Entry(master=frm_right, fg='black', bg='white',)
ent_weight.grid(row=5, column=1)
# -------------------- New Email Label ----------------
lbl_new_email = tk.Label(master=frm_right, text='Email Address: ', fg='black', width=60, height=3)
lbl_new_email.grid(row=6, column=0)
# -------------------- New Email Entry ----------------
ent_new_email = tk.Entry(master=frm_right, fg='black', bg='white',)
ent_new_email.grid(row=6, column=1)
# -------------------- New Password Label ----------------
lbl_new_password = tk.Label(master=frm_right, text='Enter Password: ', fg='black', height=3)
lbl_new_password.grid(row=7, column=0)
# -------------------- New Password Entry ----------------
ent_new_password = tk.Entry(master=frm_right)
ent_new_password.config(show="•")
ent_new_password.grid(row=7, column=1)
# -------------------- New Password Label Again ----------------
lbl_again_password = tk.Label(master=frm_right, text='Re-Enter Password: ', fg='black', height=3)
lbl_again_password.grid(row=8, column=0)
# -------------------- New Password Entry Again ----------------
ent_again_password = tk.Entry(master=frm_right)
ent_again_password.config(show="•")
ent_again_password.grid(row=8, column=1)

# -------------------- Submit Button ----------------
btn_register = tk.Button(master=frm_right, text='Change', fg='black', bg='white', height=1, width=20)
btn_register.grid(row=9, column=1)


# mainloop
window.mainloop()