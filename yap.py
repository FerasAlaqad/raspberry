from Tkinter import *
from picamera import PiCamera

redAWB = 0.29
blueAWB = 4.43
AWBsliderRes = 0.01
brightnessSliderRes = 1
gains = (redAWB,blueAWB)
camera = PiCamera() 
#camera.exposure_mode = 'off'
camera.vflip = True
camera.hflip = True
camera.resolution = (800, 600)
camera.framerate = 15
#camera.shutter_speed = camera.exposure_speed
#camera.drc_strength = "high"



   
def takePicture():
    camera.capture("testAWB.jpg", )

def takeYuvPicture():
    camera.capture("testAWB.data", "yuv")


def repos(val):
    previewX = master.winfo_x()
    previewY = master.winfo_y()    
    camera.start_preview(fullscreen=False,resolution=(400,300),window=(0,0,400,300))    

def exposure():
        camera.exposure_mode=exposureMode.get().lower()

def drc():
        camera.drc_strength=drcMode.get().lower()

def mode(val):
        #flicker()
        exposure()
        drc()

master = Tk()
master.attributes("-fullscreen", True)
previewX = master.winfo_x()
previewY = master.winfo_y()

camera.start_preview(fullscreen=False,window=(previewX+75,previewY+350,800,600))


btn = Button(master, text="Take Picture", command = takePicture)
btn.place(x=450, y=350)



master.bind("<Configure>", repos)
master.bind("<Return>", mode)
mainloop()
