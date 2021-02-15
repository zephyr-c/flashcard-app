from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
NEW_LANGUAGE = "French"

# ---------------------------- NEW CARD ------------------------------- #
language_dataframe = pd.read_csv("data/french_words.csv")
to_learn = language_dataframe.to_dict(orient="records")
current_card = random.choice(to_learn)

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(flashcard, image=flashcard_front)
    canvas.itemconfigure(title, text=NEW_LANGUAGE, fill='black')
    canvas.itemconfigure(word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfigure(flashcard, image=flashcard_back)
    canvas.itemconfigure(title, text="English", fill='white')
    canvas.itemconfigure(word, text=current_card['English'], fill='white')

def remove_seen_word():
    global current_card
    to_learn.remove(current_card)
    to_learn_dataframe = pd.DataFrame(to_learn)
    to_learn_dataframe.to_csv("data/words_to_learn.csv")
    new_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_back = PhotoImage(file="images/card_back.png")
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard = canvas.create_image(400, 263, image=flashcard_front, anchor="center")
title = canvas.create_text(400, 150, text=NEW_LANGUAGE, font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove_seen_word)
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
