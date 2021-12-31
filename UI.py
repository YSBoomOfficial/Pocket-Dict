import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
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

### handlers ###
# Display results on screen
def display_results(results: list[str]):
    # clear any already displayed results
    result_list.delete(0, END)

    # add each result to the end of the listbox
    for i in range(0, len(results)-1):
        result_list.insert(END, results[i])

# tap handler for clear button
def clear_handler():
    result_list.delete(0, END)
    field_output.set("")

# tap handler for search button
def search_handler():
    # show error if field is empty
    if field_output.get().lower().strip() == "":
        showerror(
            title='Error',
            message="No text to translate."
        )
        return

    ##### FILTER NOUN NOT WORKING #####
    # __only_nouns = True if only_nouns.get() == "1" else False

    # convert StringVar to bool, use private variable to avoid namespace collision
    __show_less = True if show_less.get() == "1" else False

    ##### FILTER NOUN NOT WORKING #####
    # data = sh.get_result(field_output.get().lower().strip(), __only_nouns, __show_less)

    data = sh.get_result(field_output.get().lower().strip(), __show_less)

    # show error if data returned is empty
    if data == []:
        showerror(
            title='Oops! Something went wrong',
            message=f"No translation found for \"{field_output.get()}\".\nTry unchecking some of the checkboxes to widen the scope."
        )
        return
    else:
        display_results(data)

### UI components ###
# create listbox for results
result_list = tk.Listbox(frame)

# Label to introduce pocket dict
intro_label = ttk.Label(
    frame,
    text="Welcome to Pocket Dict, what would you like me to translate today?",
    font=("Helvetica", 16),
    justify="center"
)

# Entry field for user input
field = ttk.Entry(
    frame,
    justify="left",
    textvariable=field_output
)
field.focus()


# search button
search_btn = ttk.Button(
    frame,
    text="Search",
)
search_btn.configure(command=search_handler)


# clear button
clear_btn = ttk.Button(
    frame,
    text="Clear",
)
clear_btn.configure(command=clear_handler)

# checkbox for fewer translations
less_box = ttk.Checkbutton(
    frame,
    text='Show Fewer Translations',
    variable=show_less,
    onvalue=True,
    offvalue=False,
    command=search_handler
)

##### FILTER NOUN NOT WORKING #####
# checkbox for only nouns
# noun_box = ttk.Checkbutton(
#     frame,
#     text='Only Show Nouns',
#     variable=only_nouns,
#     onvalue=True,
#     offvalue=False
# )

# pack all the widgets
intro_label.pack(**options)
field.pack(**options)
search_btn.pack(**options)
clear_btn.pack(**options)
less_box.pack(**options)

##### FILTER NOUN NOT WORKING #####
# noun_box.pack(**options)

result_list.pack(**options)

# add frame to root
frame.pack(**options)


# def main():
root.mainloop()
