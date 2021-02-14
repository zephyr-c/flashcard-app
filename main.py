from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashcard_front, anchor="center")
canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

# Labels
# language_name = Label(text="French")
# language_name.config(font=(FONT_NAME, 40, "italic"), bd=0, justify="center")
# language_name.place(x=400, y=150)
#
# word_name = Label(text="trouve")
# word_name.config(font=(FONT_NAME, 60, "bold"), bd=0)
# word_name.place(x=400, y=263)







window.mainloop()
