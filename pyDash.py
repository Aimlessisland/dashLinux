from PIL import Image, ImageTk
import tkinter as tk
import keyboard
import roundRect

screenWidth = 1024
screenHeight = 600

#input

def getRpm():
    #Pulse Counter generate in microsecond rpm / 2
    return rpm
def getSpeed():
    #Calculate using voltge gererate from motor //AnalogRead(A0)
    return speed
def getGear():
    return 1

def drawCenterbox():

    width = 250
    height = 250

    x1 = (screenWidth/2) - (width/2)
    x2 = x1 + width
    y1 = (screenHeight / 2) - (height/2)
    y2 = y1 + height
    roundRect.create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="white", width=3)



root = tk.Tk()
root.title("Dashboard")
root.geometry(f"{screenWidth}x{screenHeight}")
canvas = tk.Canvas(root, width=screenWidth, height=screenHeight, bg="black")
canvas.pack()
canvas.create_rectangle(0, 0, screenWidth, screenHeight, fill="black", outline="black")

def close_window(event):
    root.destroy()

if __name__ == "__main__":

    drawCenterbox()    

    root.bind('<Return>', close_window)
    root.mainloop()