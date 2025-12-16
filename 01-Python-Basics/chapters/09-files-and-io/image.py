import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

# ---------------------------------------
# CREATE TKINTER WINDOW
# ---------------------------------------
root = tk.Tk()
root.title("Image Display")
root.geometry("600x500")

# ---------------------------------------
# IMAGE PATH
# ---------------------------------------
image_path = "appu.jpg"

# ---------------------------------------
# CHECK IF FILE EXISTS
# ---------------------------------------
if not os.path.exists(image_path):
    print(f"❌ Error: '{image_path}' not found.")
    root.destroy()
    sys.exit()

# ---------------------------------------
# OPEN IMAGE USING PIL
# ---------------------------------------
image = Image.open(image_path)

# Optional: resize image
image = image.resize((400, 300))

# Convert PIL image → Tkinter image
image_tk = ImageTk.PhotoImage(image)

# ---------------------------------------
# DISPLAY IMAGE IN LABEL
# ---------------------------------------
label = tk.Label(root, image=image_tk)
label.pack(pady=20)

# ---------------------------------------
# START GUI LOOP
# ---------------------------------------
root.mainloop()
