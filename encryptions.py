"""
    project : Building a password Manager using Tkinter and the Canvas , this project will store your Data in a file
    * we will store our information in the JSON format , JSON stand for JavaScript Object Notation
    Some information :
            1- write :  json.dump() , it requires the dict variable and also the file name
            2- read  : json.load()  , it requires just the file name
            3- append : json.update()
"""
from tkinter import *
from tkinter import messagebox
import random
import json


# Saving all the data
def save_data():
    w = str(Web_entry.get()).title()
    e = email_entry.get()
    p = password_entry.get()
    new_data = {
        w: {
            "email": e,
            "password": p
        }
    }
    if len(w) == 0 or len(e) == 0 or len(p) == 0:
        messagebox.showinfo(title="Note", message="Please don't leave any field empty")
    else:
        confirmation = messagebox.askokcancel(title="Confirmation",
                                              message=f"These are the data you enterred: \n Website : {w} \n email : {e} \n password : {p} \n Do you want to save your infos ?")
        if confirmation:
            try:
                with open("YourData.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("YourData.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating our data
                data.update(new_data)

                with open("YourData.json", "w") as data_file:
                    # appending our data into the JSON file
                    json.dump(data, data_file,
                              indent=4)  # we can add an option indent and give it a number , that will be more clear
            finally:
                Web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    website = str(Web_entry.get()).title()
    try:
        with open("YourData.json") as data_file:
            data_saved = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Sorry we didn't found and file contains")
    else:
        if website in data_saved:
            messagebox.showinfo(title=f"{website} Account",
                                message=f" Email :  {data_saved[website]['email']} \n Password :  {data_saved[website]['password']}")
        else:
            messagebox.showerror(title="ValueError", message=f"Oops No details for {website} exists")
        Web_entry.delete(0, END)


def password_encrypted():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    store_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    store_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    store_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_stored = store_symbols + store_numbers + store_letters
    random.shuffle(password_stored)
    password = "".join(password_stored)
    password_entry.insert(0, password)


# tkinter configurations
window = Tk()
window.minsize(630, 580)
window.maxsize(630, 580)
window.config(bg="white", padx=25, pady=25)
window.iconbitmap('C:\\Users\\Ziraoui_Anas\\Desktop\\resume\\Advanced_Encryption\ico.ico')
window.title("Password Manager")

# canvas configurations
img_encrypt = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=img_encrypt)

canvas.place(x=180, y=70)
# Entry Configurations
Web_entry = Entry(window, text="", font=("courier", 12))
Web_entry.place(x=250, y=300, width=180)
Web_entry.focus()
email_entry = Entry(window, text="", font=("courier", 12))
email_entry.place(x=250, y=350, width=290)
password_entry = Entry(window, text="", font=("courier", 12))
password_entry.place(x=250, y=400)

# Labels configuration
Label(window, text="Secure your passwords from hackers !", font=("courier", 12, "bold"), bg="white").pack()
Web = Label(window, text="Website:", font=("courier", 12), bg="White")
Web.place(x=90, y=300, width=90)
Email = Label(window, text="Username/Email:", font=("courier", 12), bg="white")
Email.place(x=90, y=350)
password = Label(window, text="Password:", font=("courier", 12), bg="white")
password.place(x=90, y=400)

# Buttons configurations
Button(window, text="Generate", font=("courier", 12), bg="white", relief=GROOVE, command=password_encrypted).place(
    x=460, y=400, width=130)
Button(window, text="Add", font=("courier", 12), bg="white", relief=GROOVE, command=save_data).place(x=145, y=460,
                                                                                                     width=160)
Button(window, text="Quit", font=("courier", 12), bg="white", relief=GROOVE, command=window.destroy).place(x=350, y=460,
                                                                                                           width=160)
Button(window, text="Search", font=("courier", 12), bg="white", relief=GROOVE, command=search).place(x=450, y=300,
                                                                                                     width=135)
window.mainloop()
