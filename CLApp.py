import search as sh
import os

def main():
    # Clear the terminal
    os.system("clear")

    # Code for Command Line App
    field_output = ""
    show_less = False

    ##### FILTER NOUN NOT WORKING #####
    # only_nouns = False

    # Introduce the app
    print("""
        ========================================================
                        Welcome to Pocket Dict!
                What would you like me to translate today?
        ========================================================
        """)

    # Main Loop
    while True:
        # Get text to translate
        field_output = input("What would you like to look up: ").lower().strip()

        # while field is empty, prompt the user again until they enter something
        while field_output == "":
            print("Please enter a word to translate.")
            field_output = input(
                "What would you like to look up: ").lower().strip()

        # while the input is greatr than 60 characters, prompt the user again until they enter a shorter string
        while len(field_output.lower().strip()) > 60:
            field_output = ""
            print("Search text too long.")
            field_output = input(
                "What would you like to look up: ").lower().strip()

        ##### FILTER NOUN NOT WORKING #####
        # check if user wants only nouns
        # should_show_nouns = input(
        #     "Do you only want nouns? (y/n): ").lower().strip()

        # runs if user enters an invalid input
        # while should_show_nouns != "y" and should_show_nouns != "n":
        #     print("Please enter y or n")
        #     should_show_nouns = input(
        #         "Do you only want nouns? (y/n): ").lower().strip()

        # asign value to only_nouns
        # only_nouns = True if should_show_nouns == "y" else False

        # check if user wants to show less
        should_show_less = input(
            "Do you want to see fewer translations or all results? (few/all): ").lower().strip()

        # runs if user enters an invalid input
        while should_show_less != "few" and should_show_less != "all":
            print("Please enter few or all")
            should_show_less = input(
            "Do you want to see fewer translations or all results? (few/all): ").lower().strip()

        # asign value to only_nouns
        show_less = True if should_show_less == "few" else False

        # fetch results
        # data = sh.get_result(field_output,
        #                     only_nouns, show_less)

        data = sh.get_result(field_output, show_less)

        if data == []:
            # show error if data returned is empty
            print("""
        ========================================================
                    Oops! Something went wrong...
                    Try setting 'only nouns' to 'n'
                                and/or
                        'show fewer' to 'all'
        ========================================================
        """)
        else:
            # display results
            print("""
        ========================================================
                        Here are your results!
        ========================================================
        """)
            for i in range(0, len(data)):
                print(f"{i+1}. {data[i]}")
            print("""
        ========================================================
        """)

        # Ask user if they want to continue
        should_continue = input(
            "Would you like to continue? (y/n): ").lower().strip()

        while should_continue != "y" and should_continue != "n":
            print("Please enter y or n")
            should_continue = input(
                "Would you like to continue? (y/n): ").lower().strip()

        if should_continue == "n":
            break
        else:
            # clear terminal again
            os.system("clear")
            continue