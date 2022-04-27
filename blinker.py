import tkinter as tk
import tkinter.font
import RPi.GPIO as GPIO
import time




# This is my event--- That is going to be processed.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# GUI Def
win = tk.Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")




def greenToggle():
    if GPIO.input(12):
        GPIO.output(12, GPIO.LOW)
        greenButton["text"] = "LED ON"
    else:
        GPIO.output(12, GPIO.HIGH)
        greenButton["text"] = "LED OFF"

def redToggle():
    if GPIO.input(16):
        GPIO.output(16, GPIO.LOW)
        redButton["text"] = "LED ON"
    else:
        GPIO.output(16, GPIO.HIGH)
        redButton["text"] = "LED OFF"

def blueToggle():
    if GPIO.input(10):
        GPIO.output(10, GPIO.LOW)
        blueButton["text"] = "LED ON"
    else:
        GPIO.output(10, GPIO.HIGH)
        blueButton["text"] = "LED OFF"


# Widgets
blueButton = tk.Button(win, text = "LED on", font = myFont, command=blueToggle, bg = "blue", height = 1, width = 5)
blueButton.grid(row=0, column=1)

redButton = tk.Button(win, text = "LED on", font = myFont, command=redToggle, bg = "red", height = 1, width = 5)
redButton.grid(row=0, column=2)

greenButton = tk.Button(win, text = "LED on", font = myFont, command=greenToggle, bg = "green", height = 1, width = 5)
greenButton.grid(row=0, column=3)



#try:
#    while 1:
#        GPIO.output(10, GPIO.HIGH)
#        time.sleep(0.25)
#        GPIO.output(10, GPIO.LOW)
#        time.sleep(0.25)
#except KeyboardInterrupt:
#    GPIO.cleanup()
