from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO
import urllib.parse

root = Tk()
root.title("Book Recommendation System")
root.geometry("1250x700")
root. config(bg="#111119")

#############################################################################################

# icon
icon_image = PhotoImage(file="Images/icon.png")
root.iconphoto(False, icon_image)
#############################################################################################

root.mainloop()