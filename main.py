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

#################################################################################################################

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

##################################################################################################################

# first frame
frame1 = Frame(root, width=150, height=240, bg="white")
frame2 = Frame(root, width=150, height=240, bg="white")
frame3 = Frame(root, width=150, height=240, bg="white")
frame4 = Frame(root, width=150, height=240, bg="white")
frame5 = Frame(root, width=150, height=240, bg="white")
frame1.place(x=160, y=350)
frame2.place(x=360, y=350)
frame3.place(x=560, y=350)
frame4.place(x=760, y=350)
frame5.place(x=960, y=350)

# Book title
text={'a1':Label(frame1, text="Book Title", font=("arial", 10), fg="green"), 'a2':Label(frame2, text="Book Title", font=("arial", 10), fg="green"), 'a3':Label(frame3, text="Book Title", font=("arial", 10), fg="green"), 'a4':Label(frame4, text="Book Title", font=("arial", 10), fg="green"), 'a5':Label(frame5, text="Book Title", font=("arial", 10), fg="green")}
text['a1'].place(x=10, y=4)
text['a2'].place(x=10, y=4)
text['a3'].place(x=10, y=4)
text['a4'].place(x=10, y=4)
text['a5'].place(x=10, y=4)

# Poster/ Image of the book
image = {'b1':Label(frame1), 'b2':Label(frame2), 'b3':Label(frame3), 'b4':Label(frame4), 'b5':Label(frame5)}
image['b1'].place(x=3, y=30)
image['b2'].place(x=3, y=30)
image['b3'].place(x=3, y=30)
image['b4'].place(x=3, y=30)
image['b5'].place(x=3, y=30)

##################################################################################################################

# second frame
frame11 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame22 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame33 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame44 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame55 = Frame(root, width=150, height=50, bg="#e6e6e6")
frame11.place(x=160, y=600)
frame22.place(x=360, y=600)
frame33.place(x=560, y=600)
frame44.place(x=760, y=600)
frame55.place(x=960, y=600)

# published date
text2 = {'a11':Label(frame11, text="date", font=('arial', 10), bg="#e6e6e6"), 'a22':Label(frame22, text="date", font=('arial', 10), bg="#e6e6e6"), 'a33':Label(frame33, text="date", font=('arial', 10), bg="#e6e6e6"), 'a44':Label(frame44, text="date", font=('arial', 10), bg="#e6e6e6"), 'a55':Label(frame55, text="date", font=('arial', 10), bg="#e6e6e6")}
text2['a11'].place(x=10, y=4)
text2['a22'].place(x=10, y=4)
text2['a33'].place(x=10, y=4)
text2['a44'].place(x=10, y=4)
text2['a55'].place(x=10, y=4)

# Rating
text3 = {'a111':Label(frame11, text="rating", font=('arial', 10), bg="#e6e6e6"), 'a222':Label(frame22, text="rating", font=('arial', 10), bg="#e6e6e6"), 'a333':Label(frame33, text="rating", font=('arial', 10), bg="#e6e6e6"), 'a444':Label(frame44, text="rating", font=('arial', 10), bg="#e6e6e6"), 'a555':Label(frame55, text="rating", font=('arial', 10), bg="#e6e6e6")}
text3['a111'].place(x=20, y=30)
text3['a222'].place(x=20, y=30)
text3['a333'].place(x=20, y=30)
text3['a444'].place(x=20, y=30)
text3['a555'].place(x=20, y=30)

##################################################################################################################

root.mainloop()