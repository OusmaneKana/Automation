import webbrowser
import os
import time
import sys


def openSite(domain):
	for site in domain:
		webbrowser.open("https:{}.com".format(site))

def openFile(file): 
	os.system("cd C:\\Users\\Ousmane Kana\\OneDrive - Houston Community College\\Fall 2020\\{} & start .".format(file))
def openApp(app):
	os.system("start {}".format(app))

def chooseClass():
	zoom =input("Do you have an Online session Today ?__")

	if zoom.lower() in ("yes", "yup"):
		os.system("cd C:\\Users\\Ousmane Kana\\AppData\\Roaming\\Zoom\\bin & start zoom.exe")

	print("\n\nWhat Class you have ?")

	selection = input(" 1- Physic Lecture \n 2- Physics Lab \n 3-Computer Organization \n -----> ")
	if selection == "1":
		webbrowser.open("https://eagleonline.hccs.edu/courses/140584")
		openFile("Phys II")
	elif selection=="2":
		webbrowser.open("https://eagleonline.hccs.edu/courses/133980")
		openFile("Phys II lab")
	elif selection =="3":
		webbrowser.open("https://eagleonline.hccs.edu/courses/141914")
		openFile("Computer Organization")

	while True: 

		addi= input("Extra tools you'll need ? \n ------>")
		if addi.lower() in ("nope", "no","nah","done"):
			break
		else:
			lstSite = addi.split(',')
			openSite(lstSite)

def GenReport():
	print("This is a quick report that gives you insight about your grades and what you need to do")


def main():
	
	
	while True:
		task= input("\n\nWhat's up? \n\t - Class \n\t - Coding \n\t - Finances \n\t - Tools\n ------> ")
		if task.lower()== "class":
			chooseClass()

		elif task.lower() in ("coding", "code"):
			os.system("subl")
			openSite(("google", "Github", "Stackoverflow"))

		
		elif task.lower() =="finances":
			os.system(" start C:\\Users\\Ousmane Kana\\OneDrive\\Finances")
			openSite(("bankofamerica","trello"))	

		elif task.lower() =="tools":
			print("SDFSDFSFDf")
			
			while True:
				name = input("What do you want open? \n ---->")
				if name.lower() in ("done", "thas it"):
					break
				else:

					openApp(name)
					continue

		elif task.lower() in ("nothing", "done", "bye"):
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
			break	

if __name__ == '__main__':
	main()



