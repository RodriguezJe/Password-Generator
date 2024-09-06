import tkinter as tk
import random
import string


def copy_to_clipboard():

    # Clear clipboard and append new password from text field
    root.clipboard_clear()
    root.clipboard_append(new_password.get("1.0", tk.END).rstrip())
    print("Item copied to clipboad")


def generate_password():

    # Get the content from the text field
    min_length = int(pass_length_spin.get())
    # hardcode booleans to include nubmers and special chars in password
    numbers = True
    special_characters = True

    # Generate new password with above parameters
    # get all letters, digits, and special characters
    letters = string.ascii_letters
    pass_numbers = ""
    special_chars = ""

    avalaible_chars = letters

    # include numbers and special characters if requested by user
    if numbers:
        pass_numbers = string.digits
        avalaible_chars += pass_numbers
    else:
        print("User does not want numbers")

    if special_characters:
        special_chars = string.punctuation
        avalaible_chars += special_chars
    else:
        print("User does not want special characters")

    password = ""
    start_new_password = ""

    # these two if statements guarantee password meets criteria
    # without going over length this was problem for shorter passwords
    if numbers:
        start_new_password = random.choice(pass_numbers)
        password += start_new_password

    if special_characters:
        start_new_password = random.choice(special_chars)
        password += start_new_password

    # generate the rest of the password
    while len(password) < min_length:
        new_pswd_char = random.choice(avalaible_chars)
        password += new_pswd_char

    print("Password length: " + str(len(password)))
    print("Your password: " + password)

    # Clear old passwords in textbox
    new_password.delete("1.0", tk.END)
    # Set field to new password
    new_password.insert(tk.END, password)


# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Password Generator")

# Set the size of the window
root.geometry("250x250")

# Passoword length label
pass_length_label = tk.Label(root, text="Password Length")
pass_length_label.pack(pady=10)

# Password length spinbox
pass_length_spin = tk.Spinbox(root, from_=5, to=50, width=10, wrap=True)
pass_length_spin.pack(pady=5)

# Generate password Button
generate_pass_button = tk.Button(
    root, text="Generate Password", command=generate_password
)
generate_pass_button.pack(pady=10)

# New Password text box
new_password = tk.Text(root, height=3, width=20)
new_password.pack(pady=10)

# Copy to Clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
