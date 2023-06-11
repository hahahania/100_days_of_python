import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from generator import create_password
import pyperclip
import json


def new_password():
    password = create_password()
    pyperclip.copy(password)
    v.set(password)


def save_data():
    website = web_name.get()
    username = user_name.get()
    password = user_password.get()
    new_data = {website: {'email': username, 'password': password}}

    if all([website, username, password]):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_name.delete(0, tk.END)
            user_name.delete(0, tk.END)
            user_password.delete(0, tk.END)
    else:
        messagebox.showinfo(
            title='Error', message='You left some fields empty!')


def load_data():
    website = web_name.get()
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='There is no data file')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(
                title=website, message=f'Email : {email}\nPassword : {password}')
        else:
            messagebox.showinfo(
                title='Error', message='There is no data about this website')


WIDTH = 500
HEIGHT = 500
BG_COLOR = '#EEE3CB'
FONT_COLOR = '#967E76'
FONT = 'Courier New'
INPUT_COLOR = '#E8DAC3'

window = tk.Tk()
window.config(padx=50, pady=50, bg=BG_COLOR)
window.title('PASSWORD MENAGER')

v = tk.StringVar()

img = Image.open('locker.gif').resize((100, 100))
image = ImageTk.PhotoImage(img)

bg = tk.Canvas(window, width=150, height=150,
               bg=BG_COLOR, highlightthickness=0)
bg.create_image(75, 50, image=image,)
bg.grid(column=1, row=0, columnspan=3)

web = tk.Label(text='Website: ', fg=FONT_COLOR,
               bg=BG_COLOR, font=(FONT, 15))
web.grid(column=1, row=2, sticky='E', pady=5)

web_name = tk.Entry(window, bg=INPUT_COLOR,
                    borderwidth=0.5, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15))
web_name.grid(column=2, row=2, sticky='WE')

search = tk.Button(window, text='Search', bg=INPUT_COLOR,
                   borderwidth=0.25, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15), command=load_data)
search.grid(column=3, row=2)

name = tk.Label(text='Email / Nickname: ', fg=FONT_COLOR,
                bg=BG_COLOR, font=(FONT, 15))
name.grid(column=1, row=3, sticky='E', pady=5)

user_name = tk.Entry(window, bg=INPUT_COLOR,
                     borderwidth=0.5, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15))
user_name.grid(column=2, columnspan=2, row=3, sticky='WE')

password = tk.Label(text='Password: ', fg=FONT_COLOR,
                    bg=BG_COLOR, font=(FONT, 15))
password.grid(column=1, row=4, sticky='E', pady=5)

user_password = tk.Entry(window, bg=INPUT_COLOR, textvariable=v,
                         borderwidth=0.5, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15))
user_password.grid(column=2, row=4,)

generate_password = tk.Button(window, text='Generate Password', bg=INPUT_COLOR,
                              borderwidth=0.25, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15), command=new_password)
generate_password.grid(column=3, row=4)

submit = tk.Button(window, text='Submit', bg=INPUT_COLOR,
                   borderwidth=0.25, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15), command=save_data)
submit.grid(row=5, column=2, pady=20)

window.mainloop()
