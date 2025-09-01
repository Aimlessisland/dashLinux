
import tkinter as tk
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

vehSpeed_width = 200
vehSpeed_height = 65


tyrePress_width = 200
tyrePress_height = 200
# Create the main window
root = tk.Tk()
root.title("1024x600 Box (Tkinter)")
# Set the window size
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
#Should be how the whole thing draw canvas same as java differ canvas new canvas 
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
canvas.pack()
canvas.create_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", outline="black")

def drawSpeed():

    x1 = (SCREEN_WIDTH/2)-(vehSpeed_width/2)
    y1 = 10
    x2 = ((SCREEN_WIDTH/2)-(vehSpeed_width/2))+vehSpeed_width
    y2 = vehSpeed_height+10
    canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white", width="3")

def drawGear():
    x1 = (SCREEN_WIDTH/2)-(tyrePress_width/2)
    y1 = 20+ (vehSpeed_height)
    x2 = ((SCREEN_WIDTH/2)-(tyrePress_width/2))+tyrePress_width
    y2 = tyrePress_height+20 + vehSpeed_height
    canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white", width="3")


drawSpeed()
drawGear()
root.mainloop()
