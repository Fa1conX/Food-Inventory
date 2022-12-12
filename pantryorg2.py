import tkinter as tk
from turtle import bgcolor

InventoryLookupFile = "Food_Inventory_python/InventoryLookup.txt"
InventoryItemList = "InventoryLookup.txt"

# Create the main window
root = tk.Tk()
root.title("Inventory Manager")


# Create a text box for inputting new items
input_label = tk.Label(root, text="Input New Item:")
input_label.pack()
input_box = tk.Entry(root)
input_box.pack()

description_label = tk.Label(root, text="product name (only for new products):")
description_label.pack()
description_input = tk.Entry(root)
description_input.pack()

# Create a button for adding items to the file

# Function that is called when the "Add Item" button is clicked
def add_item():
    # Get the text from the input box
    item = input_box.get()

    # Open the file for appending
    with open(InventoryItemList, "a") as file:
        # Write the item to the file and add a newline character
        file.write("BARCODE:" + item +  "\n")

    # Clear the input box
    input_box.delete(0, "end")

# Set the "Add Item" button's command to the add_item function


add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.config(height=5, width=15, font=("Arial", 20, "bold"), bg="green")
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
  with open(InventoryItemList, "r") as file:
    # Read the file's contents into a list of lines
    lines = file.readlines()

  # Open the file for writing
  with open(InventoryItemList, "w") as file:
    # Write each line to the file, unless it is a blank line or matches the text to be removed
    for line in lines:
      if line.strip() != entry_to_remove:
        file.write(line)


remove_button = tk.Button(root, text="Remove Item", command=remove_entry)
remove_button.config(height=5, width=15, font=("Arial", 20, "bold"), bg="red")
remove_button.pack()


# Create a button for displaying all items in the file
def ShowAllItems():
  # Open the user_input.txt file in read-only mode
  with open(InventoryItemList, "r") as file:
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
