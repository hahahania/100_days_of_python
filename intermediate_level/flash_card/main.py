import tkinter as tk
from tkinter import font as tkfont
import pandas as pd

WIDTH = 800
HEIGHT = 600
BG_COLOR = '#F4D3D3'
CARD_COLOR = '#E8A9A9'


def get_word(file, n):
    # with open(file, 'r') as f:
    #     words = list(pd.reader(f))
    #     return words[n][0],words[n][1]
    data = pd.read_csv('french_to_polish.csv')
    polish = data.iloc[n,'polish']
    french = data.iloc[n,'french']
    data = data.drop(data.index[n])
    data.to_csv(file,index=False)
    return french, polish

def learned(controller, french,polish):
    data = {
        'polish':polish,
        'french':french
    }
    df = pd.DataFrame(data)
    df.to_csv('learned.csv')
    controller.show_frame("LearningPage")


def practice(controller,french,polish):
    data = {
        'polish':polish,
        'french':french
    }
    df = pd.DataFrame(data)
    df.to_csv('to_practice.csv')
    controller.show_frame("LearningPage")


class FlashCards(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Georgia', size=25, weight="bold",)
        self.button_font = tkfont.Font(
            family='Georgia', size=18, weight="bold",)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LearningPage, CorrectAnswer, Results):
            page_name = F.__name__
            frame = F(parent=container, controller=self, )
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LearningPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_name):
        return self.frames[page_name]

class LearningPage(tk.Frame):

    def __init__(self, parent, controller):
        self.txt = tk.StringVar()
        tk.Frame.__init__(self, parent, padx=50, pady=20, bg=BG_COLOR)
        self.controller = controller
        self.label = tk.Label(self, textvariable=self.txt,
                         font=controller.title_font, bg=CARD_COLOR, padx=150, pady=100,borderwidth=1,)
        self.label.grid(column=1, row=1, columnspan=3)

        button1 = tk.Button(self, text="CHECK!",
                            command=lambda: controller.show_frame("CorrectAnswer"), highlightbackground=BG_COLOR, font=controller.button_font)

        button1.grid(column=2, row=2, pady=20)


class CorrectAnswer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, padx=50, pady=20, bg=BG_COLOR)
        self.controller = controller
        self.txt = tk.StringVar()
        label = tk.Label(self, textvariable=self.txt,
                         font=controller.title_font, bg=CARD_COLOR, padx=150, pady=100,borderwidth=1,)
        label.grid(column=1, row=1, columnspan=3)

        button1 = tk.Button(self, text="wrong :(",
                             highlightbackground=BG_COLOR, font=controller.button_font, command=lambda:practice(controller,french,polish))

        button2 = tk.Button(self, text="ok !",
                            highlightbackground=BG_COLOR, font=controller.button_font, command=lambda:learned(controller,french,polish))
        button1.grid(column=1, row=2,pady=20)
        button2.grid(column=3, row=2,pady=20)


class Results(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, textva="This is page 2",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("LearningPage"))
        button.pack()


if __name__ == "__main__":
    n = 0
    app = FlashCards()
    running = True
    while running:
        french, polish = get_word('french_to_polish.csv',n)
        app.get_page('LearningPage').txt.set(french)
        app.get_page('CorrectAnswer').txt.set(polish)
        n+=1

    app.mainloop()