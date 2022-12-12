import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Current Inventory")


# Create a text box for inputting new items
input_label = tk.Label(root, text="Input New Item:")
input_label.pack()
input_box = tk.Entry(root)
input_box.pack()



# Create a button for adding items to the file

# Function that is called when the "Add Item" button is clicked
def add_item():
    # Get the text from the input box
    item = input_box.get()

    # Open the file for appending
    with open("user_input.txt", "a") as file:
        # Write the item to the file and add a newline character
        file.write(item + "\n")

    # Clear the input box
    input_box.delete(0, "end")

# Set the "Add Item" button's command to the add_item function


add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.config(height=5, width=15, font=("Arial", 20, "bold"), activebackground="red")
add_button.pack()


# Create a text box for removing items
remove_label = tk.Label(root, text="Remove Item:")
remove_label.pack()
remove_box = tk.Entry(root)
remove_box.pack()


# Create a button for removing items from the file
def remove_entry():
  # Get the text from the text box
  entry_to_remove = remove_box.get()

  # Open the file for reading
  with open("user_input.txt", "r") as file:
    # Read the file's contents into a list of lines
    lines = file.readlines()

  # Open the file for writing
  with open("user_input.txt", "w") as file:
    # Write each line to the file, unless it is a blank line or matches the text to be removed
    for line in lines:
      if line.strip() != entry_to_remove:
        file.write(line)


"""def remove_entry():
  # Get the location of the file and the entry to remove
  file_location = 'user_input.txt'
  entry_to_remove = remove_box.get()

  # Open the file and read its contents
  with open(file_location, 'r') as file:
    file_contents = file.read()

  # Remove the entry from the file contents
  updated_file_contents = file_contents.replace(entry_to_remove, '')

  # Write the updated contents back to the file
  with open(file_location, 'w') as file:
    file.write(updated_file_contents)

  # Clear the input box
  remove_box.delete(0, "end")"""

remove_button = tk.Button(root, text="Remove Item", command=remove_entry, activebackground="red")
remove_button.pack()


# Create a button for displaying all items in the file
def ShowAllItems():
  # Open the user_input.txt file in read-only mode
  with open("user_input.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()

    # Create a new window to display the file contents
    window = tk.Toplevel(root)
    current_inventory = tk.Label(window, width=25, text=contents)
    current_inventory.pack()

show_button = tk.Button(root, text="Show All Items", command=ShowAllItems)
show_button.pack()

# Start the main event loop
root.mainloop()
