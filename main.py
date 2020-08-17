from time import *
import os

try:
    # For Python 2
    from Tkinter import *
except ImportError:
    # For Python 3
    from tkinter import *

"""
Window and canvas config
"""
top = Tk()
dead = False # Status flag
top.geometry("450x450")
top.title("Berlin Uhr")
top.iconbitmap('assets/icons/appIcon.ico')
top.resizable(height=FALSE, width=FALSE)
can = Canvas(top, bg="#eee", height=450, width=450)
can.pack()
mainLabel = Label(top, text="Berlin Uhr (Set Theory Clock)", font=("Berlin Sans FB", 17))
mainLabel.place(x=80, y=5)

# Description text for About window
description = 'Mengenlehreuhr (German for "Set Theory Clock") or\nBerlin-Uhr (German for "Berlin Clock"), ' \
              'is the first\npublic clock in the world that tells the time by means\nof illuminated, coloured fields, ' \
              'for which it entered the Guinness Book of Records upon its installation on\n17 June ' \
              '1975.\n\nCommissioned by the Senate of Berlin and designed\nby Dieter Binninger, the original ' \
              'full-sized\nMengenlehreuhr was originally located at the\nKurfürstendamm on the corner with ' \
              'Uhlandstraße.\nAfter the Senate decommissioned it in 1995, the clock was relocated to a site in ' \
              'Budapester Straße in front ofEuropa-Center, where it stands today.\n(Source: Wikipedia) '


# Defining the About window
def about_win():
    about = Toplevel(top)
    about.geometry("450x450")
    about.resizable(height=FALSE, width=FALSE)
    about_txt = Text(about, font=("Bahnschrift", 12), spacing1=4, spacing2=4)
    about_txt.insert(INSERT, description)
    about_txt['state'] = DISABLED
    about_txt.place(x=25, y=25, width=400, height=350)
    exit_btn = Button(about, text="Exit", command=about.destroy)
    exit_btn.place(x=200, y=400)


# Defining the menu bar
bar = Menu(top)
menu = Menu(bar, tearoff=0)
menu.add_command(label="About", command=about_win)
menu.add_command(label="How to read?", command=NO)
menu.add_separator()
menu.add_command(label="Exit", command=top.quit)
bar.add_cascade(label="More", menu=menu)
top.config(menu=bar)

# Colour definitions
outerCol = "#C0C0C0"  # outer silver colour for metal
innerCol = "#777"  # inner grey colour
orange = "#FFA500"  # orange colour for the lights
red = "#E22D00"  # red colour for the lights

# Shape creation
ovalBack = can.create_oval(205, 55, 245, 95, fill=outerCol)
innerOval = can.create_oval(210, 60, 240, 90, fill=innerCol)
outerRec1 = can.create_rectangle(65, 115, 385, 165, fill=outerCol)
innerRec1 = []
startPt = 70
ran = 60
for x in range(1, 5, 1):
    x0 = startPt * x + x * 8
    x1 = x0 + ran
    innerRec1.append(can.create_rectangle(x0, 122, x1, 158, fill=innerCol))

outerRec2 = can.create_rectangle(65, 185, 385, 235, fill=outerCol)
innerRec2 = []
startPt = 70
ran = 60
for x in range(1, 5, 1):
    x0 = startPt * x + x * 8
    x1 = x0 + ran
    innerRec2.append(can.create_rectangle(x0, 192, x1, 228, fill=innerCol))

outerRec3 = can.create_rectangle(65, 255, 385, 305, fill=outerCol)
innerRec3 = []
startPt = 52
ran = 20
for x in range(1, 12, 1):
    x0 = startPt + x * 27
    x1 = x0 + ran
    innerRec3.append(can.create_rectangle(x0, 262, x1, 298, fill=innerCol))

outerRec4 = can.create_rectangle(65, 325, 385, 375, fill=outerCol)
innerRec4 = []
startPt = 70
ran = 60
for x in range(1, 5, 1):
    x0 = startPt * x + x * 8
    x1 = x0 + ran
    innerRec4.append(can.create_rectangle(x0, 332, x1, 368, fill=innerCol))


def paint():
    hr = localtime()[3]
    top_hr = int(hr / 5)
    if top_hr != 0:
        for n in range(top_hr):
            can.itemconfig(innerRec1[n], fill=red)
    else:
        for n in range(top_hr):
            can.itemconfig(innerRec1[n], fill=red)

    btm_hr = hr % 5
    if btm_hr != 0:
        for n in range(btm_hr):
            can.itemconfig(innerRec2[n], fill=red)
    else:
        for n in range(4):
            can.itemconfig(innerRec2[n], fill=innerCol)

    mins = localtime()[4]
    # Top row of minutes
    top_mins = int(mins / 5)
    if top_mins != 0:
        for n in range(top_mins):
            if (n == 2) | (n == 5) | (n == 8):
                can.itemconfig(innerRec3[n], fill=red)
            else:
                can.itemconfig(innerRec3[n], fill=orange)
    else:
        for n in range(11):
            can.itemconfig(innerRec3[n], fill=innerCol)

    # Bottom row of minutes
    btm_mins = mins % 5
    if btm_mins != 0:
        for n in range(btm_mins):
            can.itemconfig(innerRec4[n], fill=orange)
    else:
        for n in range(4):
            can.itemconfig(innerRec4[n], fill=innerCol)

    secs = localtime()[5]
    if (secs % 2) == 0:
        can.itemconfig(innerOval, fill=orange)
    else:
        can.itemconfig(innerOval, fill=innerCol)
    can.after(1000, paint)


# Refresh method
def refresh():
    os.execl(sys.executable, sys.executable, *sys.argv)


# Refresh button
btnLabel2 = "Refresh"
refreshButton2 = Button(top, text=btnLabel2, command=refresh)
refreshButton2.place(x=200, y=390)


paint()
top.mainloop()
