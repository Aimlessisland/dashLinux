import tkinter as tk

def on_key_press(event, canvas, text_id):
    char = event.char
    if char.isalnum():
        canvas.itemconfig(text_id, text=char.upper())

def create_input_canvas():
    WIDTH = 1280
    HEIGHT = 700
    root = tk.Tk()
    root.title("Keyboard Input Canvas")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack(fill=tk.BOTH, expand=True)
    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    text_id = canvas.create_text(
        center_x, center_y,
        text="",
        fill="white",
        font=("Arial", 200, "bold")
    )
    root.bind("<Key>", lambda event: on_key_press(event, canvas, text_id))
    root.mainloop()

if __name__ == "__main__":
    create_input_canvas()
