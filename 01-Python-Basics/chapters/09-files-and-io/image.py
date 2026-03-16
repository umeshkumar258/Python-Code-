import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys


def load_and_display_image(window, image_path, size=(400, 300)):
    """Load an image, resize it, and display it in the Tkinter window."""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"'{image_path}' not found.")

        image = Image.open(image_path)
        image = image.resize(size)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(window, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(pady=20)

    except FileNotFoundError as error:
        messagebox.showerror("File Error", str(error))
        window.destroy()
        sys.exit()

    except Exception as error:
        messagebox.showerror("Error", f"Unable to load image:\n{error}")
        window.destroy()
        sys.exit()


# ---------------------------------------
# CREATE TKINTER WINDOW
# ---------------------------------------
root = tk.Tk()
root.title("Image Display")
root.geometry("600x500")
root.resizable(False, False)

# ---------------------------------------
# IMAGE PATH
# ---------------------------------------
image_path = "appu.jpg"

# ---------------------------------------
# LOAD AND DISPLAY IMAGE
# ---------------------------------------
load_and_display_image(root, image_path)

# ---------------------------------------
# START GUI LOOP
# ---------------------------------------
root.mainloop()
