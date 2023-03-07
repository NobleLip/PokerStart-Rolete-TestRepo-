import pywintypes
#import pythoncom # Uncomment this if some other DLL load will fail
import win32gui
import pyautogui
import time
import random


def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x+30, y+y1*0.6635, 40, 1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im


def ReturnColor(im):
	for x in range(im.width):
		XLine = im.getpixel((x, 0))
		if XLine[0] > 130 and XLine[0]==XLine[1]==XLine[2]:
			return ("Black")
		elif XLine[0] > 150 and XLine[0]!=XLine[1] and XLine[0]!=XLine[2]:
			return ("Red")
		
def CheckIfDif(Newim, Oldim):
	for x in range(Newim.width):
		if Newim.getpixel((x,0)) != Oldim.getpixel((x,0)):
			return True
	return False

#ScreenTo = win32gui.GetWindowText(win32gui.GetForegroundWindow())

NewIMAGE = True

#Probability counter
Black = 0
Red = 0

Cash = 5
time.sleep(2)
userin = win32gui.GetForegroundWindow()

BetB = 0.1
BetR = 0.1
BolBetB = False
BolBetR = False

while True:
	time.sleep(1)
	if NewIMAGE:
			im = screenshot(win32gui.GetWindowText(userin))
			#im.show()
			Color = ReturnColor(im)
			print("[+] New Color : "+ str(Color))

			if Color == "Black":
				if BolBetR:
					Cash = Cash + BetR
					print("[+] Cash ADDED : "+ str(Cash))
				Red = 0
				Black = Black + 1
				BetB = 0.1
				RedProb = (100 - (0.5**(Black+1)*100))
				print("		[+] Black Probability : "+ str(100-RedProb))
				print("		[+] Red Probability : "+ str(RedProb))
				if RedProb > 99 :
					if Cash >= BetR:
						BolBetB = True
						Cash = Cash - BetR
						BetR = BetR * 2
					else:
						print("[!] Lost More than winning")
						break
			elif Color == "Red":
				if BolBetB:
					Cash = Cash + BetB
					print("[+] Cash ADDED : "+Cash)
				Black=0
				BetR = 0.1
				Red = Red + 1
				BlackProb = (100- (0.5**(Red+1)*100))
				print("		[+] Black Probability : "+str(BlackProb))
				print("		[+] Red Probability : "+str(100-BlackProb))
				if BlackProb > 99 :
					if Cash >= BetR:
						BolBetR = True
						Cash = Cash - BetB
						BetB = BetB * 2
					else:
						print("[!] More than winning")
						break

			NewIMAGE = False
	NewIMAGE = CheckIfDif(im, screenshot(win32gui.GetWindowText(userin)))


"""
class info():
	def __init__(self):
		self.Cash = 5
		self.Black = 0
		self.Red = 0
		self.BetR = 0.1
		self.BetB = 0.1
		self.BolBetR = False
		self.BolBetB = False
		self.BlackProb = 0
		self.RedProb = 0


def RoletPick():
	#			  0   1   2   3   4   5   6   7   8   9   10  11  12 13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36
	RoletaInf = ["G","R","B","R","B","R","B","R","B","R","B","B","R","B","R","B","R","B","R","R","B","R","B","R","B","R","B","R","B","B","R","B","R","B","R","B","R"]
	Num = random.randint(0,len(RoletaInf)-1)
	return (Num, RoletaInf[Num])

Prob = []
for i in range(0,37):
	Prob.append(0)

WalletInf = info()

while True:
	NumColor = RoletPick()

	if WalletInf.RedProb >= 99:
		if WalletInf.BolBetR:
			WalletInf.BetR = WalletInf.BetR * 2
		if WalletInf.Cash >= WalletInf.BetR:
			WalletInf.Cash = WalletInf.Cash - WalletInf.BetR
			print("[-] Bet on Red : "+str(WalletInf.BetR)+ "  Probability : "+str(WalletInf.RedProb))
		else:
			print("[!] This Probability is Not Viable")
		WalletInf.BolBetR = True

	elif WalletInf.BlackProb >= 99:
		if WalletInf.BolBetB:
			WalletInf.BetB = WalletInf.BetB * 2
		if WalletInf.Cash >= WalletInf.BetB:
			WalletInf.Cash = WalletInf.Cash - WalletInf.BetB
			print("[-] Bet on Black : "+str(WalletInf.BetB)+ "  Probability : "+str(WalletInf.BlackProb))
		else:
			print("[!] This Probability is Not Viable")
		WalletInf.BolBetB = True

	if NumColor[1] == "B":
		if WalletInf.BolBetB:
			WalletInf.BolBetB = False
			WalletInf.Cash = WalletInf.Cash + WalletInf.BetB
			print("[+] "+ str(WalletInf.BetB)+ " ADDED TO WALLET   CASH = "+ str(WalletInf.Cash))
			WalletInf.BetB = 0.1

		WalletInf.Red = 0
		WalletInf.Black = WalletInf.Black + 1

		#Probabilitys
		WalletInf.BlackProb = (0.5**WalletInf.Black*100)
		WalletInf.RedProb = 100 - WalletInf.BlackProb

		print("[!] Color Black , Times : "+str(WalletInf.Black)+" Probability : "+str(WalletInf.BlackProb))

	elif NumColor[1] == "R":
		if WalletInf.BolBetR:
			WalletInf.BolBetR = False
			WalletInf.Cash = WalletInf.Cash + WalletInf.BetR
			print("[+] "+ str(WalletInf.BetR)+ " ADDED TO WALLET   CASH = "+str(WalletInf.Cash))
			WalletInf.BetR = 0.1

		WalletInf.Black = 0
		WalletInf.Red = WalletInf.Red + 1
		#Probabilitys
		WalletInf.RedProb = (0.5**WalletInf.Red*100)
		WalletInf.BlackProb = 100 - WalletInf.RedProb

		print("[!] Color Red , Times : "+str(WalletInf.Red)+" Probability : "+str(WalletInf.RedProb))

"""