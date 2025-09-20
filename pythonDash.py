from PIL import Image, ImageTk
import tkinter as tk
import keyboard

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

righBox_width = 370
righBox_height =250

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

    #Engine rpm will just use str() to convert number to it. Will need input later to variated number
    engineRPM = 6500

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
        text=str(engineRPM), 
        fill="white", 
        font=("sans-serif", int(vehSpeed_height * 0.7), "bold")
    )

def drawGear(indicateGear):

    gearIndicate = indicateGear
    x1 = (SCREEN_WIDTH / 2) - (gearIndi_width / 2)
    y1 = 10 + vehSpeed_height+5
    x2 = x1 + gearIndi_width
    y2 = y1 + gearIndi_height
    # Use the custom function to draw a rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="white", width=3)

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    
    # Draw the letter "N" in the center, sized to nearly fit the box
    text_id = canvas.create_text(
        center_x, 
        center_y, 
        text=gearIndicate,
        fill="yellow", 
        font=("sans-serif", int(gearIndi_height * 0.8), "bold")
    )
    root.bind("<Key>", lambda event: on_key_press(event, canvas, text_id))


def on_key_press(event, canvas, text_id):
    char = event.char
    if char.isalnum():
        canvas.itemconfig(text_id, text=char.upper())

def create_input_canvas():
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    text_id = canvas.create_text(
        center_x, center_y,
        text="",
        fill="white",
        font=("Arial", 200, "bold")
    )
    root.bind("<Key>", lambda event: on_key_press(event, canvas, text_id))
    

def drawtyrePress():
    x1 = (SCREEN_WIDTH / 2) - (gearIndi_width / 2)
    y1 = 10 + vehSpeed_height + gearIndi_height+10
    x2 = x1 + tyrePress_width
    y2 =  y1 + tyrePress_height
    # Use the custom function to draw a rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="orange", width=3)

    canvas.create_text(
        SCREEN_WIDTH / 2,
        y1 + 25,
        text="TYRE PRESSURE",
        fill="orange",
        font=("sans-serif", 21, "bold")
    )

        # Tyre pressure values
    frontLeft = "145"
    frontRight = "146"
    backLeft = "147"
    backRight = "148"
    font_size = 25
    
    # Calculate positions for the four pressure values
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    frontPos = 35
    backPos = 55
    
    # Front-left tire pressure
    canvas.create_text(
        center_x - 40,
        center_y - frontPos,
        text=frontLeft,
        fill="white",
        font=("sans-serif", font_size, "bold"),
        anchor="ne"
    )
    
    # Front-right tire pressure
    canvas.create_text(
        center_x + 40,
        center_y - frontPos,
        text=frontRight,
        fill="white",
        font=("sans-serif", font_size, "bold"),
        anchor="nw"
    )
    
    # Back-left tire pressure
    canvas.create_text(
        center_x - 40,
        center_y + backPos,
        text=backLeft,
        fill="white",
        font=("sans-serif", font_size, "bold"),
        anchor="se"
    )
    
    # Back-right tire pressure
    canvas.create_text(
        center_x + 40,
        center_y + backPos,
        text=backRight,
        fill="white",
        font=("sans-serif", font_size, "bold"),
        anchor="sw"
    )

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
        ("Water temp", "85°C"),
        ("Water press", "1.1 BAR"),
        ("Turbo press", "15 PSI")
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
        
        canvas.create_text(
            x1 + padding, 
            y_pos, 
            text=label, 
            fill="yellow", 
            font=text_font, 
            anchor="w"
        )
        
        canvas.create_text(
            x2 - padding, 
            y_pos, 
            text=value, 
            fill="white", 
            font=text_font, 
            anchor="e"
        )


def drawRightbox():
    x1 = 15 + liquid_width + gearIndi_width + 10
    y1 = 10 + vehSpeed_height + 5
    x2 = x1 + righBox_width
    y2 = y1 + righBox_height
    
    # Draw the rounded rectangle
    create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, outline="white", width=3)
    right_aligned_x = x2 - 20 
    center_y = (y1 + y2) / 2
    main_font_size = int(righBox_height * 0.5)
    small_font_size = int(righBox_height * 0.1) 

    # Create the main "120" text, right-aligned
    canvas.create_text(
        right_aligned_x,
        center_y - 50, # Shift it slightly up
        text="120",
        fill="white",
        font=("sans-serif", main_font_size, "bold"),
        anchor="e" # Align to the east (right)
    )

    # Create the small "KM/H" text, also right-aligned
    canvas.create_text(
        right_aligned_x,
        center_y + 35, # Shift it down, below the main text
        text="KM/H",
        fill="white",
        font=("sans-serif", small_font_size),
        anchor="e" # Align to the east (right)
    )
    
    global fuel_icon
    image = Image.open("fuel.png")
    image = image.resize((30, 30))
    root.fuel_icon = ImageTk.PhotoImage(image)
    canvas.create_image(x1+25+5, y2-25, image=root.fuel_icon)
    fuel_square_size = 30
    fuel_padding = 5  # Spacing between the squares
    num_squares = 8  # Number of squares to draw

    # The starting x position for the first square, to the right of the fuel icon
    start_x = x1 + 25 + 5 + 30 + 5 
    square_y = y2 - 25 - (fuel_square_size / 2)

    # Loop to draw each square
    for i in range(num_squares):
        # Calculate the x coordinates for the current square based on the loop index
        current_x1 = start_x + (fuel_square_size + fuel_padding) * i
        current_x2 = current_x1 + fuel_square_size

        # Create the rectangle with a white fill
        canvas.create_rectangle(
            current_x1,
            square_y,
            current_x2,
            square_y + fuel_square_size,
            fill="white",
            outline="white",
            width=2
        )
    
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

def drawHeadLight():
    global headlight_image
    image = Image.open("headlight.png")
    image = image.resize((50, 50)) 
    root.headlight_image = ImageTk.PhotoImage(image)
    canvas.create_image(liquid_width - 22, 52, image=root.headlight_image)

def drawHighbeam():
    global highbeam_image
    image = Image.open("highbeam.png")
    image = image.resize((50, 50)) 
    root.highbeam_image = ImageTk.PhotoImage(image)
    canvas.create_image(liquid_width - 80, 50, image=root.highbeam_image)

def drawHandbrake():
    global handbrake_image
    image = Image.open("handbrake.png")
    image = image.resize((40, 35)) 
    root.handbrake_image = ImageTk.PhotoImage(image)
    canvas.create_image(liquid_width - 135, 50, image=root.handbrake_image)

def drawlowBrake():
    global lowbrake_image
    image = Image.open("lowbrakefluid.png")
    image = image.resize((42
                          , 35)) 
    root.lowbrake_image = ImageTk.PhotoImage(image)
    canvas.create_image(liquid_width - 185, 50, image=root.lowbrake_image)

def close_window(event):
    root.destroy()

def drawMode():
    x1 = (liquid_width + gearIndi_width) + 60
    canvas.create_text(x1, 60, text="ECO", fill="green", font=("sans-serif", 20, "bold"))

if __name__ == "__main__":
    drawRpm()
    drawGear("N")
    drawtyrePress()
    drawLiquid()
    drawRightbox()
    drawLeftarrow()
    drawRightarrow()
    drawHeadLight()
    drawHighbeam()
    drawHandbrake()
    drawlowBrake()
    drawMode()
    # Start the Tkinter event loop
    root.bind('<Return>', close_window)
    root.mainloop()

