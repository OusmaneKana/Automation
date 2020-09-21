import webbrowser
import os
import time
def openSite(domain):
	for site in domain:
		webbrowser.open("https:{}.com".format(site))

def openFile(file): 
	os.system("cd C:\\Users\\Ousmane Kana\\OneDrive - Houston Community College\\Fall 2020\\{} & start .".format(file))
def openApp(app):
	os.system("start {}".format(app))

def chooseClass():
	print("What Class you have ?")

	selection = input("1- Physic Lecture \n2- Physics Lab \n 3-Computer Organization \n ----->")
	if selection == "1":
		webbrowser.open("https://eagleonline.hccs.edu/courses/140584")
		openFile("Phys II")
	elif selection=="2":
		webbowser.open("https://eagleonline.hccs.edu/courses/133980")
		openFile("Phys II lab")
	elif selection =="3":
		webbrowser.open("https://eagleonline.hccs.edu/courses/141914")
		openFile("Computer Organization")

	while True: 

		addi= input("Extra tools you'll need ? \n ------>")
		if addi in ("Nope", "no","nah"):
			break
		else:
			openSite(addi)


def main():
	
	
	while True:
		task= input("\nWhat's up? \n ------>")
		if task.lower()== "class":
			chooseClass()

		elif task.lower() == "code":
			os.system("subl")
			openSite(("google", "Github", "Stackoverflow"))

			pass
		
		elif task.lower() =="finances":
			os.system(" start C:\\Users\\Ousmane Kana\\OneDrive\\Finances")
			openSite(("bankofamerica","trello"))	

		elif task.lower() =="tools":
			
			while True:
				name = input("What do you want open? \n ---->")
				if name in ("Done", "thas it"):
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
			print("\n\n ****** DO NOT QUITE!***** \n\n")
			time.sleep(2)
			break	

if __name__ == '__main__':
	main()



