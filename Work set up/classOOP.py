
import datetime
import webbrowser
import os
import time
import sys


class Class:

	def __init__(self, name, sites, tools ="NONE"):
		self.name = name 
		self.sites = sites
		self.tools = tools 
	def openSite(self):
		for site in self.sites:
			webbrowser.open("https:www.{}.com".format(site))
	def openTools(self):
		pass


dataMining = Class("Data Mining", ("stackoverflow", "google", "github", ))
systemProgramming = Class("Data Mining", ("stackoverflow", "google", "github", ))
discreateMath = Class("Data Mining", ("stackoverflow", "google", "github", ))
statistics =  Class("Data Mining", ("stackoverflow", "google", "github", ))
programmingLanguagues = Class("Data Mining", ("stackoverflow", "google", "github",))

taskrn = input("What do you have now ?")

m = getattr(taskrn, 'openSite')

m()


