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

# background image
heading_image = PhotoImage(file="Images/background.png")
Label(root, image=heading_image, bg="#111119").place(x=-2, y=-2)

# logo
logo_image = PhotoImage(file="Images/logo.png")
Label(root, image=logo_image, bg="#0099ff").place(x=300, y=80)

# heading
heading = Label(root, text="BOOK RECOMMENDATION", font=("Lato", 30, "bold"), fg="white", bg="#0099ff")
heading.place(x=410, y=90)

# search bar
search_box = PhotoImage(file="Images/Rectangle 2.png")
Label(root, image=search_box, bg="#0099ff").place(x=300, y=155)

# entry box / search section
Search = StringVar()
search_entry = Entry(root, textvariable=Search, width=20, font=("Lato", 25), bg="white", fg="black", bd=0)
search_entry.place(x=415, y=172)

# search button
recommend_button_image = PhotoImage(file="Images/Search.png")
recommend_button = Button(root, image=recommend_button_image, bg="#0099ff", bd=0, activebackground="#252532", cursor="hand1")
recommend_button.place(x=860, y=169)

# setting button
Setting_image = PhotoImage(file="Images/setting.png")
setting = Button(root, image=Setting_image, bd=0, cursor="hand2", activebackground="#0099ff", bg="#0099ff")
setting.place(x=1050, y=175)

# logout button
Logout_image = PhotoImage(file="Images/logout.png")
Button(root, image=Logout_image, bg="#0099ff", cursor="hand1", command=lambda: root.destroy()).place(x=1150, y=20)

#############################################################################################

root.mainloop()