import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, END, LEFT
from tkinter.messagebox import showerror
import search as sh

# init the root window and set its title
root = tk.Tk()
root.title("Pocket Dict")

# set the frame
frame = ttk.Frame(root)
options = {'padx': 10, 'pady': 10}

# init variables that we will need for Field and checkboxes
field_output = tk.StringVar()
only_nouns = tk.StringVar()
show_less = tk.StringVar()

# centre the window on screen
window_width = root.winfo_screenwidth() // 2
window_height = root.winfo_screenheight() // 2

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create listbox for results and set scrollbar
scrollbar = ttk.Scrollbar(frame)
scrollbar.grid(row=3, column=0)
result_list = tk.Listbox(frame, yscrollcommand=scrollbar.set)
result_list.grid(row=3, column=0)
scrollbar.config(command=result_list.yview)

# Label to introduce pocket dict
intro_label= ttk.Label(
    frame,
    text="Welcome to Pocket Dict, what would you like me to translate today?",
    font=("Helvetica", 16),
    justify="center"
)
intro_label.grid(row=0, column=0, **options)

# Entry field for user input
field = ttk.Entry(
    frame,
    justify="left",
    textvariable=field_output
)
field.grid(row=1, column=0)
field.focus()

def display_results(results: list[str]):
    for i in range(0, len(results)-1):
        result_list.insert(END, results[i])

# tap handler for search button
def search_handler():
    # show error if field is empty
    if field_output.get() == "":
        showerror(
            title='Error',
            message="No text to translate."
        )
        return

    # convert StringVar to bool, use private variable to avoid namespace collision
    __only_nouns = True if only_nouns.get() == "1" else False
    __show_less = True if show_less.get() == "1" else False

    data = sh.get_result(field_output.get(), __only_nouns, __show_less)

    print(field_output.get())
    print(__only_nouns)
    print(__show_less)

    # show error if data returned is empty
    if data == []:
        showerror(
            title='Oops! Something went wrong',
            message=f"No translation found for \"{field_output.get()}\".\nTry unchecking some of the checkboxes to widen the scope."
        )
        return
    else:
        print(data)
        display_results(data)

# search button
btn = ttk.Button(
    frame,
    text="Search",
)
btn.grid(row=2, column=0, **options)
btn.configure(command=search_handler)

# tap handler for clear button
def clear_handler():
    result_list.delete(0, END)
    field_output.set("")

# clear button
btn = ttk.Button(
    frame,
    text="Clear",
)
btn.grid(row=2, column=1, **options)
btn.configure(command=clear_handler)

# checkbox for fewer translations
ttk.Checkbutton(
    frame,
    text='Show Fewer Translations',
    variable=show_less,
    onvalue=True,
    offvalue=False
).grid(row=2, column=2, **options)

# checkbox for only nouns
ttk.Checkbutton(
    frame,
    text='Only Show Nouns',
    variable=only_nouns,
    onvalue=True,
    offvalue=False
).grid(row=2, column=3, **options)

# add frame to root
frame.grid(padx=10, pady=10)
root.mainloop()
