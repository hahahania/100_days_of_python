import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from generator import create_password
import pyperclip

WIDTH = 500
HEIGHT = 500
BG_COLOR = '#EEE3CB'
FONT_COLOR = '#967E76'
FONT = 'Courier New'
INPUT_COLOR = '#E8DAC3'


def new_password():
    password = create_password()
    pyperclip.copy(password)
    v.set(password)


def collect_data():
    website = web_name.get()
    username = user_name.get()
    password = user_password.get()

    if all([website, username, password]):
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            web_name.delete(0, tk.END)
            user_name.delete(0, tk.END)
            user_password.delete(0, tk.END)
            with open('data.txt', 'w') as file:
                file.write(f'{website} | {username} | {password}\n')
    else:
        popup = tk.Tk()
        label = tk.Label(popup, text=f'No field should be empty')
        label.pack()
        button = tk.Button(popup, text='Close', command=popup.destroy)
        button.pack()


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
web_name.grid(column=2, columnspan=2, row=2, sticky='WE')

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
                   borderwidth=0.25, highlightthickness=0, fg=FONT_COLOR, font=(FONT, 15), command=collect_data)
submit.grid(row=5, column=2, pady=20)

window.mainloop()
