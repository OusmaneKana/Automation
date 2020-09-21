from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as Bsoup
from IPython.display import Image 


def parse_page(url):

	x = Ureq(url)
	page = x.read()
	x.close()
	page_parsed = Bsoup(page, 'html.parser')
	
	return (page_parsed)



def main(search):

	parsed_page = parse_page("https://houston.craigslist.org/search/sss?query={}".format(search))
	
	container= parsed_page.findAll("li", {"class": "result-row"})

	for i in range(9):
		print(container[i].a["href"])
		print(container[i].findAll("a",{"class":"result-title hdrlnk"})[0].text)
		print(container[i].findAll("span",{"class":"result-price"})[0].text)
		print("----------------------------")


  

if __name__ == '__main__':
	search = input("What do you want to search? :\n ------->")
	print("\n\n\n")
	main(search)




	

