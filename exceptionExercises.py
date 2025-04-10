# Exercises for Exceptions

# All of these functions should accept a prompt, a default value and a help text.

class UserQuit (Exception):
    pass


menu = ["Latte", "Cappuccino", "Flat White", "Black Americano",
        "White Americano", "Filter Coffee", "Double Espresso"]

print(f"Please select your coffee from the menu! {menu}")


def ckmenuItem(prompt, help=""):
    # Checking the input for a valid menu item. Will raise UserQuit.
    valid = False
    while not valid:
        try:
            a = input(prompt + "[q, ?]")
        except EOFError:
            raise UserQuit
        if a.title() in menu:
            valid = True
        elif a.title() in ["Q", "QUIT"]:
            raise UserQuit
        elif a.title() in ["?"]:
            print(help)
        elif a.title() not in menu:
            print("You've entered an invalid input, please try again")
    return a


try:
    a = ckmenuItem("What would you like to drink?",
                   "Remember you can only order one coffee at a time!")
    print(
        f"Thanks for your order! ({a}) \nPlease wait whilst we make your coffee!")

# Still have to handle the error that has been raised from the function in an except clause.
except UserQuit:
    print("You quit the ordering process. Goodbye!")

finally:
    print("Thank you for visiting our coffee shop!")
