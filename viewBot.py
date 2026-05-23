import webbrowser

import time

import os

inpt = input("Enter url here ")

inpt2 = float(input("Enter refresh rate(seconds): "))

inp4 = int(input("Enter views: "))
#make it an realitic amout since it can lead in a ban if not.
print("hello")
counter =0
while (counter != inp4):
	webbrowser.open(inpt)
	time.sleep(inpt2)
	webbrowser.close()
	counter = counter +1
	
