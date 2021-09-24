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

def Register():
    # check all fields completed
    # check email is valid
    # check password is valid
    # check age is valid
    # check height is valid (i.e not a string)
    # check weight is valid (i.e not a string)
    # check passwords match
    # save information in database
    con = sqlite3.connect('Data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO record VALUES (:name, :age, :gender, :height, :weight, :email, :password)", {
        'name': ent_new_name.get(),
        'age': ent_age.get(),
        'gender': var.get(),
        'height': ent_height.get(),
        'weight': ent_weight.get(),
        'email': ent_new_email.get(),
        'password': ent_new_password.get()
})
    con.commit()
    ent_new_name.delete(0, tk.END)
    ent_age.delete(0, tk.END)
    ent_height.delete(0, tk.END)
    ent_weight.delete(0, tk.END)
    ent_new_email.delete(0, tk.END)
    ent_new_password.delete(0, tk.END)
    ent_new_password_again.delete(0, tk.END)

con = sqlite3.connect('Data.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
    name text,
    age number,
    gender text,
    height number,
    weight number,
    email text,
    password text)
''')
con.commit()

# -------------------- Left Frame ----------------
frm_left = tk.Frame(master=window)
frm_left.grid(row=0, column=0)
# -------------------- Email Label ----------------
lbl_email = tk.Label(master=frm_left, text='Email Address: ', fg='black', width=60, height=3)
lbl_email.grid(row=0, column=0)
# -------------------- Email Entry ----------------
ent_email = tk.Entry(master=frm_left, fg='black', bg='white')
ent_email.grid(row=0, column=1)
# -------------------- Password Label ----------------
lbl_password = tk.Label(master=frm_left, text='Enter Password: ', fg='black', height=3)
lbl_password.grid(row=1, column=0)
# -------------------- Password Entry ----------------
ent_password = tk.Entry(master=frm_left)
ent_password.config(show="•")
ent_password.grid(row=1, column=1)
# -------------------- Verification Label ----------------
lbl_verification = tk.Label(master=frm_left, text='', fg='red', height=3)
lbl_verification.grid(row=2, column=0, padx=10, pady=10)
# -------------------- Submit Button ----------------
btn_submit = tk.Button(master=frm_left, text='Login', fg='black', bg='white', height=1, width=20)
btn_submit.grid(row=2, column=1)

# --------------------- Right Frame ----------------
frm_right = tk.Frame(master=window)
frm_right.grid(row=0, column=1)

lbl_register = tk.Label(master=frm_right, text='Register', fg='black', width=60, height=5)
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
btn_register = tk.Button(master=frm_right, text='Register', fg='black', bg='white', height=1, width=20, command = Register)
btn_register.grid(row=9, column=1)

def BMI():
    bmi = weight / height^2 #(kg/meters^2)
'''under<18.5, normsl =18.5-24.9, over = 25-29.9, obese = 30 or greater'''

# --------------------- Events ----------------

ALLOWED_DOMAINS = ['com', 'co', 'uk', 'ac', 'bham']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

def verify_email(email_address, error_text):
    if '@' in email_address:
        split_list = email_address.split('@')
        after_at_list = split_list[1].split('.')
        part_list = after_at_list[1:]

        for part in part_list:
            if part not in ALLOWED_DOMAINS:
                error_text = 'Invalid address - one or more domains not allowed'
    else:
        error_text = 'Invalid address - please enter an @ symbol'

    return error_text

def verify_password(password, error_text):
    if not password.islower() and not password.isupper():
        num_exists = False
        for char in password:
            if char in NUMBERS:
                num_exists = True
                break

        if num_exists == False:
             error_text = 'Invalid password - please use numbers'

    else:
         error_text = 'Invalid password - cannot use all upper or lower case letters'

    return error_text

def submit_pressed(event):
    error_text='Success!'
    email_address = ent_email.get()
    error_text = verify_email(email_address, error_text)
    if error_text != 'Success!':
        lbl_verification['text'] = error_text
    else:
        password = ent_password.get()
        error_text = verify_password(password, error_text)
        lbl_verification['text'] = error_text
        if error_text == 'Success!':
            lbl_verification['fg'] = 'green'
            window.destroy()
            import Menu
        else:
            print('Log-in failed')
btn_submit.bind("<Button-1>", submit_pressed)


# mainloop
window.mainloop()
