from tkinter import*
import tkinter.font

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Hardware
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

# GUI Definitions
win =Tk()
win.title("LED TOGGLER")
myFont=tkinter.font.Font(family='Helvitica', size=12, weight="bold")

#Event Functions 
def ledToggle1():
	if (GPIO.input(5) == GPIO.HIGH): #gpio.input(36) == high
		GPIO.output(5,GPIO.LOW) #gpio.output(36)== low
		ledButton1["text"]="Turn Red Led On"
	else:
		GPIO.output(5,GPIO.HIGH)
		ledButton1["text"]="Turn Red Led Off"
def ledToggle2():
	if (GPIO.input(6) == GPIO.HIGH):
		GPIO.output(6,GPIO.LOW)
		ledButton2["text"]="Turn Yellow Led On"
	else:
		GPIO.output(6,GPIO.HIGH)
		ledButton2["text"]="Turn Yellow Led Off"	
def ledToggle3():
	if (GPIO.input(13) == GPIO.HIGH):
		GPIO.output(13,GPIO.LOW)
		ledButton3["text"]="Turn Green Led On"
	else:
		GPIO.output(13,GPIO.HIGH)
		ledButton3["text"]="Turn Green Led Off"	
		

# Menu Widgets
ledButton1= Button(win,text="Turn Red Led On",font=myFont, command =ledToggle1, bg='bisque2',height=2,width=24)
ledButton1.grid(row=0,column=1)

ledButton2= Button(win,text="Turn Yellow Led On",font=myFont, command =ledToggle2, bg='bisque2',height=2,width=24)
ledButton2.grid(row=1,column=1)

ledButton3= Button(win,text="Turn Green Led On",font=myFont, command =ledToggle3, bg='bisque2',height=2,width=24)
ledButton3.grid(row=2,column=1)

exitButton= Button(win,text="Exit",font=myFont, command =exit, bg='red',height=2,width=6)
exitButton.grid(row=3,column=1)

