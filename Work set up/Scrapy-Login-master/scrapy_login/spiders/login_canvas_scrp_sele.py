# -*- coding: utf-8 -*-
from scrapy import Spider
import os
from scrapy.http import FormRequest
from selenium import webdriver
from scrapy.utils.response import open_in_browser


class QuotesSpider(Spider):
	name = 'canvas'
	start_urls = ['https://eagleonline.hccs.edu/login/ldap']


	def __init__(self):
		self.em= os.environ.get('my_em')
		self.pw=os.environ.get('my_pw')

		self.driver.get('https://eagleonline.hccs.edu/login/ldap')
		self.driver.find

	def parse(self, response):
		token =  response.xpath('//input[@type="hidden"]/@value')[1].extract()
		open_in_browser(response)
		print("*************\n\n The token is", token)
		return FormRequest.from_response(response,
														formdata={
														'utf8': "✓",
														'authenticity_token': token,
														'redirect_to_ssl': "1",
														'pseudonym_session[unique_id]': "",
														'pseudonym_session[password]': "",
														'pseudonym_session[remember_me]': "0"
													},callback=self.scrape_pages, dont_filter = True)




	def scrape_pages(self, response):
		print("****************** New Reposne is",response)
		open_in_browser(response)