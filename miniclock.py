import tkinter as tk
from time import strftime
from tkinter import font as tkfont

def time():
    """Update the clock label with the current time."""
    string = strftime('%I:%M:%S%p')  # Format the time as 12-hour with AM/PM
    label.config(text=string)
    label.after(1000, time)  # Call this function again after 1000ms (1 second)

def on_drag_start(event):
    """Start dragging the window."""
    root.x = event.x
    root.y = event.y

def on_drag_motion(event):
    """Move the window during dragging."""
    delta_x = event.x - root.x
    delta_y = event.y - root.y
    new_x = root.winfo_x() + delta_x
    new_y = root.winfo_y() + delta_y
    root.geometry(f'+{new_x}+{new_y}')

# Create the main window
root = tk.Tk()
root.title("Mini Digital Clock")

# Remove window border and title bar
root.overrideredirect(True)

# Make the window always on top
root.attributes('-topmost', True)

# Set the dimensions and style of the window
width = 112
height = 40
root.geometry(f"{width}x{height}")

# Calculate initial position (center-right of the screen with padding)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - width - 20  # 20 pixels from the right edge
y = (screen_height // 2) - (height // 2)  # Center vertically

root.geometry(f"{width}x{height}+{x}+{y}")
root.configure(bg='black')  # Background color

# Create a font with fallback
def get_font(family, size, weight='normal'):
    try:
        return tkfont.Font(family=family, size=size, weight=weight)
    except tkfont.TclError:
        return tkfont.Font(family='Arial', size=size, weight=weight)

# Use the custom font function
custom_font = get_font('Poppins', 13, 'bold')

# Create the time label with the custom font
label = tk.Label(root, font=custom_font, background='black', foreground='white')
label.pack(expand=True)  # Center the label within the window

# Call the time function
time()

# Make the window draggable
label.bind('<Button-1>', on_drag_start)
label.bind('<B1-Motion>', on_drag_motion)

# Run the Tkinter event loop
root.mainloop()