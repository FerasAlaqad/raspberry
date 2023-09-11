import tkinter as tk
from picamera import PiCamera

# Constants for camera settings
RED_AWB = 0.29
BLUE_AWB = 4.43

# Initialize the PiCamera
camera = PiCamera()
camera.vflip = True
camera.hflip = True
camera.resolution = (800, 600)
camera.framerate = 15

def take_picture():
    """Capture an image and save it as 'testAWB.jpg'."""
    camera.capture("testAWB.jpg")

def exit_application():
    """Exit the application."""
    exit()

def start_preview(val):
    """Start the camera preview with specified resolution and position."""
    camera.start_preview(fullscreen=False, resolution=(800, 480), window=(0, 0, 800, 480))

def set_exposure():
    """Set the camera exposure mode."""
    exposure_mode = exposure_mode_var.get().lower()
    camera.exposure_mode = exposure_mode

def set_drc():
    """Set the camera DRC strength."""
    drc_strength = drc_strength_var.get().lower()
    camera.drc_strength = drc_strength

def main():
    """Main function to create and run the GUI."""
    root = tk.Tk()
    root.title("Raspberry Pi Camera GUI")
    root.attributes("-fullscreen", True)
    root.configure(background='black')

    # Create and place widgets
    img = tk.PhotoImage(file='logo.png')
    logo = tk.Label(root, image=img)
    logo.place(x=640, y=50)

    capture_button = tk.Button(root, text="Capture", command=take_picture, height=5, width=17)
    capture_button.place(x=640, y=150)

    exit_button = tk.Button(root, text="Exit", command=exit_application, height=5, width=17)
    exit_button.place(x=640, y=350)

    # Bind events
    root.bind("<Configure>", start_preview)
    root.bind("<Return>", lambda event: (set_exposure(), set_drc()))

    root.mainloop()

if __name__ == "__main__":
    exposure_mode_var = tk.StringVar()
    drc_strength_var = tk.StringVar()

    main()
