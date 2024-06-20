import tkinter as tk
import tkinter.font as tkFont

def populate_fonts(text_widget):
    fonts = list(tkFont.families())
    for font in fonts:
        text_widget.insert(tk.END, f"This is {font}\n", font)
        text_widget.tag_configure(font, font=(font, 12))

root = tk.Tk()
root.title("Font Display")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(expand=1, fill=tk.BOTH)

populate_fonts(text_widget)

root.mainloop()
