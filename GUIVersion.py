import tkinter
from tkinter import *

import current as current
from tkintermapview import TkinterMapView

#Display window,size & background color
root =tkinter.Tk()
root.title("AIS Console")
root.geometry("1000x1000")
root.config(bg="white")

#Top Label
l1=Label(root, text="File      Help      Data Columns")
l1.place(x=0, y=0)

#Button
b1=Button(root, text="Select COM", width=10)
b1.place(x=0, y=21)


b2=Button(root, text="Diagnostics", width=10)
b2.place(x=80, y=21)

b3=Button(root, text="Send data", width=10)
b3.place(x=160, y=21)

b4=Button(root, text="Received data", width=13)
b4.place(x=240, y=21)

b5=Button(root, text="Map", width=7,)
b5.place(x=341, y=21)


b6=Button(root, text="Close", width=41, command=quit)
b6.place(x=696, y=758)


#Text Box
text_box = tkinter.Entry(root)
text_box.place(x=695, y=200, width=300, height=550)
text_box.config(background="grey")


def Lat_long():
   Lt=float(E1.get())
   Lg=float(E2.get())
   map_widget = TkinterMapView(root, width=300, height=585)
   map_widget.place(x=5, y=200, width=680, height=585)
   map_widget.set_position(Lt, Lg, marker=True)
   map_widget.set_zoom(17)

l1=Label(root, text="Enter Latitude", font=('Calibri 10'))
l1.place(x=10, y=120)
E1=Entry(root, width=20)
E1.place(x=110, y=120)

l2=Label(root, text="Enter Longitude", font=('Calibri 10'))
l2.place(x=10,y=150)
E2=Entry(root, width=20)
E2.place(x=110, y=150)


l3=Label(root, text="Enter your coordinate : ", font=('Calibri 14'))
l3.pack(pady=20)
l3.place(x=10, y=70)

B1=Button(root, width=15, text="Find", command=Lat_long)
B1.place(x=260, y=150)

root.mainloop()
