from tkinter import *

# -----------------Disappearing Text 5000 logic -------------------- #


def start_app():
    welcome_label.grid_forget()
    start_button.grid_forget()
    textbox.grid(row=3, column=1, padx=10, pady=10)
    textbox.focus()


def disappear_text():
    textbox.delete(1.0, END)
    textbox.insert(END, "")


def check_disappear():
    global counter, text
    if text == textbox.get(1.0, END):
        if counter == 10:
            window.after(1000, disappear_text)
            counter = -1
        window.after(1000, check_disappear)
        counter += 1
    else:
        window.after(1000, check_disappear)
        text = textbox.get(1.0, END)
        counter = 0


# -----------------Gui-------------------- #

window = Tk()
window.iconbitmap("Disappearing Text App/Assets/text.ico")
window.title("Disappearing Text 5000")
window.config(pady=20, padx=20)

welcome_label = Label(text="Welcome to the Disappearing text app, write something or within 10 seconds "
                           "the text you've wrote will disappear.")
welcome_label.grid(column=1, row=1, pady=6)

start_button = Button(text="Start!", command=start_app)
start_button.grid(column=1, row=2)

text = ""
counter = 0
textbox = Text(height=10, width=40)

window.after(1000, check_disappear)
window.mainloop()
