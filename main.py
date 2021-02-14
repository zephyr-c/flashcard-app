from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
flashcard_front = PhotoImage("images/card_front.png")
canvas.create_image(400, 250, image=flashcard_front)
canvas.pack()








window.mainloop()
