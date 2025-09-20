import tkinter as tk
from PIL import Image, ImageTk
import os

# Create the Tkinter window
root = tk.Tk()
root.title("Image Display")

# Define the image path
image_path = "appu.jpg"

# Try to open the image file using Pillow
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found. Please check the file path.")
    root.destroy()
    exit()

# Convert the image to a format Tkinter can use
image_tk = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = tk.Label(root, image=image_tk)
label.pack()

# Start the Tkinter event loop
root.mainloop()
