import tkinter as tk


window = tk.Tk()
window.minsize(width= 300, height=100)

text_input = tk.Entry(width=10)
text_input.grid(row=0,column=1)

miles = tk.Label(text='miles')
miles.grid(row=0,column=2)

to = tk.Label(text = 'is equal to')
to.grid(row=1,column=0)

result = tk.Label(text = '0')
result.grid(row=1,column=1)

km = tk.Label(text='km')
km.grid(row=1,column=2)

def convert():
    miles = float(text_input.get())
    kilomiters = str(round(miles*1.609, 1))
    result.config(text=kilomiters)
    

button = tk.Button(text='Convert', command=convert)
button.grid(row=2,column=1)


window.mainloop()