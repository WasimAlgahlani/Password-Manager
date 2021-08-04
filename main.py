from tkinter import *
from tkinter import messagebox
import password
import json
import pyperclip


def check_empty():
    if len(web_input.get()) == 0 or len(pass_input.get()) == 0 or len(email_user_input.get()) == 0:
        return True
    return False


def save_data():
    if check_empty():
        messagebox.showinfo(title="website data", message="You left some entries empty")
    else:
        new_data = {web_input.get().title(): {"email": email_user_input.get(), "password": pass_input.get()}}

        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
        messagebox.showinfo(title="website data", message="Saved successfully")


def search_web():
    if len(web_input.get()) == 0:
        messagebox.showinfo(title="website data", message="You must enter the name of the website")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="error", message="File not found")
        else:
            if web_input.get().title() not in data:
                messagebox.showinfo(title="website data", message="There is no such saved website")
            else:
                messagebox.showinfo(title="website data",
                                    message=f"email: {data[web_input.get().title()]['email']}\npassword:{data[web_input.get().title()]['password']}")


def generate():
    pass_input.insert(0, password.password)
    pyperclip.copy(password.password)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img_name = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=img_name)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
web_label.config(pady=5)

web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()

web_button = Button(text="Search", width=15, command=search_web)
web_button.grid(row=1, column=2)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
email_user_label.config(pady=5)

email_user_input = Entry(width=40)
email_user_input.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_label.config(pady=5)

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)

pass_gen = Button(text="Generate Password", command=generate)
pass_gen.grid(row=3, column=2)

pass_add = Button(text="Add", width=36, command=save_data)
pass_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
