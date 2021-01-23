""" Important Xxpath:

Login Page: https://offerup.com/accounts/login/

Login Button:  /html/body/div[1]/div[1]/div/div/div/div[3]/ul/li[2]/div/div/div/a[1]/div/span

UserName: /html/body/div[1]/div/div[2]/div/div/div/form/div[1]/div[1]/div/div/input

PassWord: /html/body/div[1]/div/div[2]/div/div/div/form/div[1]/div[2]/div/div/input
"""


from selenium import webdriver 
import os



def Launch(myid, mypassword):
	cwd = os.getcwd()
	print(cwd)
	driver = webdriver.Firefox(executable_path=cwd+f'\geckodriver.exe')
	driver.get("https://offerup.com/accounts/login/")
	driver.find_element_by_id('db-email-input').send_keys(myid)
	driver.find_element_by_id('db-password-input').send_keys(mypassword)
	driver.find_element_by_class_name('db-submit-btn').click()




def main ():

	user = input("What is the User Name:   ")
	PassWord = input("What's the pwd:     ")


	Launch(user, PassWord)


if __name__ == '__main__':
	main()