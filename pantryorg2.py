import tkinter as tk
from turtle import bgcolor
import requests

InventoryLookupFile = "InventoryLookup.txt"
InventoryItemList = "InventoryItemList.txt"

# Create the main window
root = tk.Tk()
root.title("Inventory Manager")


# Create a text box for inputting new items
input_label = tk.Label(root, text="Barcode scan:")
input_label.pack()
input_box = tk.Entry(root)
input_box.pack()

def auto_run(event):
    # Get the input text from the input box
    input_text = event.widget.get()

    # Check if the input text is 12 characters long
    if len(input_text) == 12:
        add_item()
input_box.bind("<Key>", auto_run)

def add_item():
    # Get the text from the input box
    item = input_box.get()

    # Open the file for appending
    with open(InventoryItemList, "a") as file:
        # Write the item to the file and add a newline character
        file.write("UPC: " + item +  "\n")

    # Clear the input box
    input_box.delete(0, "end")

####

# Replace with your own API key
API_KEY = 'YOUR_API_KEY'
"""
# Function to look up a UPC code using the UPCitemdb API
def lookup_upc(upc_code, api_key):
  # Construct the URL for the API request
  url = 'https://api.upcitemdb.com/prod/trial/lookup'
  params = {
    'upc': upc_code,
  }

  # Make the request to the UPCitemdb API
  response = requests.get(url, params=params)

  # Parse the JSON response
  response_json = response.json()

  # Extract the information about the item from the response
  item = response_json['items'][0]
  title = item['title']
  brand = item['brand']
  description = item['description']
  image_url = item['images'][0]

  # Print the information about the item
  print(f'Title: {title}')
  print(f'Brand: {brand}')
  print(f'Description: {description}')
  print(f'Image URL: {image_url}')

# Look up a UPC code
lookup_upc('0123456789', API_KEY)

####
"""

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.config(height=2, width=10, font=("Arial", 20, "bold"), bg="green")
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
remove_button.config(height=2, width=10, font=("Arial", 20, "bold"), bg="red")
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
