import tkinter as tk
import random
dvd = "./DVD_Icon/DVD.png"

root = tk.Tk()
root.geometry("960x540")

image = tk.PhotoImage(file=dvd)
picture_label = tk.Label(root, image=image)
x,y = random.randint(0,910), random.randint(0,515)

picture_label.place(x=x,y=y)

x_movement = random.choice([1, -1])
y_movement = random.choice([1, -1])

def movement():

    global x, y, x_movement, y_movement

    if x in [0,910] and y in [0, 515]:
        
        yay = tk.Label(root, text="yay!", font=("", 64), fg="#0B6E0B")
        yay.pack(pady=200)

        def yay_remove():
            yay.destroy()

        root.after(1000, yay_remove)

    if x in [0, 910]:
        x_movement *= -1
    if y in [0, 515]:
        y_movement *= -1

    x += x_movement
    y += y_movement

    picture_label.place(x=x, y=y)

    root.after(5, movement)

movement()

root.mainloop()