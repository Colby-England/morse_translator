from tkinter import *
from morse_translator import engl_to_morse
from morse_translator import morse_to_engl

root = Tk()

frame_text_a = Frame()
text_a = Text(master=frame_text_a)
label_a = Label(master=frame_text_a, text="Enter text to translate here.")
label_a.pack()
text_a.pack()

frame_text_b = Frame()
translation = StringVar(frame_text_b)
translation.set("Translation:")
label_b = Label(master=frame_text_b, textvariable=translation)
label_b.pack()

frame_options = Frame()
start_language = StringVar(frame_options)
start_language.set("English")  # initial value
label_b = Label(master=frame_options, text="Select Starting Language:")
option = OptionMenu(frame_options, start_language, "English", "Morse")
label_b.pack(side="left")
option.pack(side="left")


def translate():
    language = start_language.get()
    phrase = text_a.get("1.0", END).replace("\n", "")
    if language == "English":
        trans = engl_to_morse(phrase)
    else:
        trans = morse_to_engl(phrase)
    translation.set(trans)


frame_translate = Frame()
btn_translate = Button(frame_translate, text="Translate", command=translate())
btn_translate.pack(side="bottom")

frame_options.pack()
frame_text_a.pack()
frame_translate.pack()
frame_text_b.pack()

root.mainloop()