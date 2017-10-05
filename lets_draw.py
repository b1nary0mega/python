import pyautogui
import time

#Global variables
drawSpeed = .5
typeSpeed = .5

#displayStyles are f,t,c
#f = fullscreen (stretch)
#t = tiled
#c = centered
def makeWallpaper(displayStyle):
	if(displayStyle != 'f'):
		print("DisplayStyle " + displayStyle + " not acceptable.")
		system.exit()

	#make the image our new wallpaper
	pyautogui.hotkey('alt', 'f')
	pyautogui.press('b')
	pyautogui.press(displayStyle) #select FILL for wallpaper

#Open up paint
def openPaint():
	#open up MSPaint
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite('mspaint', 0)
	pyautogui.press('enter')
	time.sleep(1)

#Write out our image file
#overwrite: n = no | y = yes
def saveImage(imgSaveName, overwrite):
	#save the image
	pyautogui.hotkey('alt', 'f')
	pyautogui.press('s')
	time.sleep(.5)
	pyautogui.typewrite(imgSaveName)
	time.sleep(.5)
	pyautogui.press('enter')
	time.sleep(.5)
	pyautogui.press(overwrite) #overwrite image if it already exists
	time.sleep(.5)

#close the paint window
def closePaint():
	#exit out of the program
	pyautogui.hotkey('alt', 'f4')

#Resize the canvas to provided size
def resizePaintCanvas(width, height):
	#resize the mspaint window
	pyautogui.hotkey('ctrl', 'w')
	pyautogui.press('right') #by pixels
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('space') #don't maintain aspect
	pyautogui.hotkey('shift', 'tab')
	pyautogui.hotkey('shift', 'tab')
	pyautogui.typewrite(str(width), typeSpeed) #set horizontal
	pyautogui.press('tab')
	pyautogui.typewrite(str(height), typeSpeed) #set vertical
	pyautogui.press('enter')

#draw a nice square spiral
def drawSpiral(width, height, lineSpacing):
	#draw a spiral, starting in the center of the screen (not the center of the canvas!)
	pyautogui.moveTo(width/2, height/2)

	distance = width/4

	while distance > 0:
		pyautogui.dragRel(distance, 0, duration=drawSpeed) #move right
		distance = distance - lineSpacing
		pyautogui.dragRel(0, distance, duration=drawSpeed) #move down
		pyautogui.dragRel(-distance, 0, duration=drawSpeed) #move left
		distance = distance - lineSpacing
		pyautogui.dragRel(0, -distance, duration=drawSpeed) #move up

#Main method
def main():
	#determine screensize
	xsize = pyautogui.size()[0]
	ysize = pyautogui.size()[1]
	print('Screensize detected: ' + str(xsize) + ' x ' + str(ysize))

	openPaint()

	resizePaintCanvas(xsize, ysize)

	drawSpiral(xsize, ysize, 25)

	saveImage('%DEFAULTUSERPROFILE%\mynewbg.png','y')

	makeWallpaper('f')

	closePaint()

main()
