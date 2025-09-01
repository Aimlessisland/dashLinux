from PIL import Image, ImageTk
import tkinter as tk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
   
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, smooth=True, **kwargs)
    
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

vehSpeed_width = 250
vehSpeed_height = 65

gearIndi_width = 250
gearIndi_height = 250

tyrePress_width = 250
tyrePress_height = 150

liquid_width = 370
liquid_height = 250

lapTime_width = 370
lapTime_height =250

# Create the main window
root = tk.Tk()
root.title("Dashboard")

# Set the window size
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# Create the canvas
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
canvas.pack()
# Draw the background
canvas.create_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", outline="black")

def drawRpm():
    """Draws the vehicle speed box with rounded corners."""
    x1 = (SCREEN_WIDTH / 2) - (vehSpeed_width / 2)
    y1 = 10
    x2 = x1 + vehSpeed_width
    y2 = y1 + vehSpeed_height
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=15, outline="white", width=3)
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    canvas.create_text(
        center_x, 
        center_y, 
        text="6500", 
        fill="white", 
        font=("sans-serif", int(vehSpeed_height * 0.7), "bold")
    )

def drawGear():
    """Draws the gear display box with rounded corners."""
    x1 = (SCREEN_WIDTH / 2) - (gearIndi_width / 2)
    y1 = 10 + vehSpeed_height+5
    x2 = x1 + gearIndi_width
    y2 = y1 + gearIndi_height
    # Use the custom function to draw a rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="white", width=3)

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Draw the letter "N" in the center, sized to nearly fit the box
    canvas.create_text(
        center_x, 
        center_y, 
        text="N", 
        fill="yellow", 
        font=("sans-serif", int(gearIndi_height * 0.8), "bold")
    )

def drawtyrePress():
    x1 = (SCREEN_WIDTH / 2) - (gearIndi_width / 2)
    y1 = 10 + vehSpeed_height + gearIndi_height+10
    x2 = x1 + tyrePress_width
    y2 =  y1 + tyrePress_height
    # Use the custom function to draw a rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="orange", width=3)

def drawLiquid():
    x1 = 10
    y1 = 10 + vehSpeed_height + 5
    x2 = x1 + liquid_width
    y2 = y1 + liquid_height
    # Use the custom function to draw a rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="white", width=3)

    data = [
        ("Oil temp", "95°C"),
        ("Oil press", "2.5 BAR"),
        ("Water temp", "85"),
        ("Water press", "1.1 BAR")
    ]
    
    padding = 20
    font_size = 20
    text_font = ("sans-serif", font_size)
    line_spacing = font_size + 15
    # Calculate the total height of the text block
    total_text_height = (len(data) - 1) * line_spacing

    # Calculate the vertical start position to center the text block
    start_y = y1 + (y2 - y1) / 2 - total_text_height / 2
    
    # Loop through the data and draw text
    for i, (label, value) in enumerate(data):
        # Calculate y position for the current line
        y_pos = start_y + (i * line_spacing)
        
        # Draw the left-aligned label
        canvas.create_text(
            x1 + padding, 
            y_pos, 
            text=label, 
            fill="yellow", 
            font=text_font, 
            anchor="w"
        )
        
        # Draw the right-aligned value
        canvas.create_text(
            x2 - padding, 
            y_pos, 
            text=value, 
            fill="white", 
            font=text_font, 
            anchor="e"
        )


def drawLaptime():
    x1 = 15 + liquid_width + gearIndi_width + 10
    y1 = 10 + vehSpeed_height +5
    x2 = x1 + lapTime_width
    y2 = y1 + lapTime_height
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius = 20, outline = "white", width=3)
# Call the drawing functions
def drawLeftarrow():
    global tk_image 
    image = Image.open("arrow.png")
    image = image.resize((50, 50))
    image = image.transpose(Image.FLIP_LEFT_RIGHT) 
    root.tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(25+5, 50, image=root.tk_image)

def drawRightarrow():
    global tk_image2 
    image = Image.open("arrow.png")
    image = image.resize((50, 50))
    root.tk_image2 = ImageTk.PhotoImage(image)
    canvas.create_image(SCREEN_WIDTH - (25+5), 50, image=root.tk_image2)

drawRpm()
drawGear()
drawtyrePress()
drawLiquid()
drawLaptime()
drawLeftarrow()
drawRightarrow()
# Start the Tkinter event loop
root.mainloop()
