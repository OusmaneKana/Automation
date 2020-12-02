from selenium import webdriver 



def Login(myid, mypassword):
	driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe')
	driver.get("https://eagleonline.hccs.edu/login/ldap")
	driver.find_element_by_id('pseudonym_session_unique_id').send_keys(myid)
	driver.find_element_by_id('pseudonym_session_password').send_keys(mypassword)
	driver.find_element_by_class_name('Button--login').click()



def main ():

	myid = input("what us your email ya akhi--->    ")
	mypassword = input("what is your password ya akhi--->    ")
	Login(myid, mypassword)


if __name__ == '__main__':
	main()