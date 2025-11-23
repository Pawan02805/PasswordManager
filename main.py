from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4)) ]

    password_list = password_symbol+password_letter+password_number

    shuffle(password_list)

    password_input.delete(0,END)
    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent= 4)

        finally:
            website_entry.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH SETUP ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no entry for {website}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady = 20, bg= "white")

canvas = Canvas(height= 200, width= 200, bg= "white", highlightthickness= 0)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(115,100, image= logo_img)
canvas.grid(row = 0, column = 1)

label_website = Label(text = "Website:", bg = "white")
label_website.grid(row = 1, column= 0)

label_username = Label(text= "Email/Username:", bg = "white")
label_username.grid(row = 2, column= 0)

label_password = Label(text= "Password:", bg = "white")
label_password.grid(row = 3, column = 0 )

button_generate = Button(text= "Generate Password", bg = "white", command= generate_pass)
button_generate.grid(row=3, column= 2)

button_add = Button(text= "Add", width=55, bg = "white", command= save_password)
button_add.grid(row = 4, column= 1, columnspan= 2)

search_button = Button(text="Search", bg = "blue", width= 13, command= find_password)
search_button.grid(row=1, column= 2)

website_entry = Entry(width=45)
website_entry.grid(row=1, column= 1)
website_entry.focus()

email_entry = Entry(width=65)
email_entry.grid(row=2, column= 1, columnspan=2)
email_entry.insert(0,"pythonprojecttest@gmail.com")



password_input = Entry(width=45)
password_input.grid(row=3, column= 1)





window.mainloop()