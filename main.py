from time import *

try:
    # For Python 2
    from Tkinter import *
except ImportError:
    # For Python 3
    from tkinter import *

top = Tk()
top.geometry("450x450")
top.title("Berlin Uhr Clock")
top.iconbitmap(r'C:\Users\amir1\Downloads\good.ico')
can = Canvas(top, bg="#eee", height=450, width=450)
can.pack()

outerCol = "#C0C0C0"  # outer silver colour for metal
innerCol = "#777"  # inner grey colour
orange = "#FFA500"  # orange colour for the lights
red = "#E22D00"  # red colour for the lights

mainLabel = Label(top, text="Berlin Uhr Clock", font=("Arial", 20))
mainLabel.place(x=125, y=5)

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


paint()
top.mainloop()
