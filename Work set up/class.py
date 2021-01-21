import webbrowser
import os
import time
import sys


def openSite(domain):
	for site in domain:
		webbrowser.open("https:www.{}.com".format(site))

def openFile(file): 
	os.system("cd C:\\Users\\Ousmane Kana\\OneDrive - North American University\\Spring 2021\\{} & start .".format(file))
def openApp(app):
	os.system("start {}".format(app))

def chooseClass():
	webbrowser.open("https://portal.na.edu/ics")
	webbrowser.open("https://www.office.com/")
	zoom =input("Do you have an Online session Today ?__")

	if zoom.lower() in ("yes", "yup"):
		print ("Which class ?")
		selection = input(" 1- Data Mining\n 2- Discrete Math \n 3-Programming Language \n 4 -Statistics \n 5-System Programming  \n -----> ")
		selection = selection.split(',')
		for course in selection:
			if course =="1":
				webbrowser.open("https://global.gotomeeting.com/join/213951021")
			if course =="2":
				webbrowser.open("https://www.gotomeet.me/hnguye01/math2317_spring2021")
			if course =="3":
				webbrowser.open("https://global.gotomeeting.com/join/894151789")
			if course =="4":
				webbrowser.open("https://www.gotomeet.me/hnguye01/math1312_spring2021")
			if course =="5":
				webbrowser.open("https://global.gotomeeting.com/join/408824989")
			



	print("\n\nWhat Class you have ?")

	selection = input(" 1- Data Mining\n 2- Discrete Math \n 3-Programming Language \n 4 -Statistics \n 3-System Programming  \n -----> ")
	if selection == "1":
		webbrowser.open("https://eagleonline.hccs.edu/courses/140584")
		openFile("Phys II")
	elif selection=="2":
		webbrowser.open("https://eagleonline.hccs.edu/courses/133980")
		openFile("Phys II lab")
	elif selection =="3":
		webbrowser.open("https://eagleonline.hccs.edu/courses/141914")
		openFile("Computer Organization")
	elif selection =="4":
		webbrowser.open("https://eagleonline.hccs.edu/courses/141914")
		openFile("Computer Organization")
	elif selection =="5":
		webbrowser.open("https://eagleonline.hccs.edu/courses/141914")
		openFile("Computer Organization")

	while True: 

		addi= input("Extra tools you'll need ? \n ------>")
		if addi.lower() in ("nope", "no","nah","done"):
			break
		else:
			lstSite = addi.split(',')
			openSite(lstSite)


def appClose():
	time.sleep(1)
	print("\n\n ****** ENJOY YOUR WORK ***** \n\n")
	time.sleep(1)
	print("\n\n ****** BE PRODUCTIVE ***** \n\n")
	time.sleep(1)
	print("\n\n ****** But most importantly ***** \n\n")
	time.sleep(1)
	print("\n\n ****** DO ***** \n\n")
	time.sleep(0.75)
	print("\n\n ****** NOT ***** \n\n")
	time.sleep(0.75)
	print("\n\n ******!!!! QUIT !!!!***** \n\n")
	time.sleep(4)
		


def main():
	
	
	while True:
		task= input("\n\nWhat's up? \n\t - Class \n\t - Coding \n\t - Finances \n\t - Tools \n ----> ")
		if task.lower()== "class":
			chooseClass()

		elif task.lower() in ("coding", "code"):
			os.system("subl")
			openSite(("google", "Github", "Stackoverflow"))

		
		elif task.lower() =="finances":
			os.system(" start C:\\Users\\Ousmane Kana\\OneDrive\\Finances")
			openSite(("bankofamerica","trello"))	

		elif task.lower() =="tools":
		
			while True:
				name = input("What do you want open? \n ---->")
				if name.lower() in ("done", "thas it"):
					break
				else:

					openApp(name)
					continue






		elif task.lower() in ("nothing", "done", "bye"):
			appClose()
			

if __name__ == '__main__':
	main()



