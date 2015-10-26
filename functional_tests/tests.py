from django.test import LiveServerTestCase
from unittest import skip

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SOTestCase(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	@skip("")
	def test_we_can_reach_front_page_and_login(self):
		""" Test that front page is working and we can log in successfully """
		self.browser.get('%s%s' % (self.live_server_url, '/'))
		# Check the title while we're here
		self.assertTrue("LaserCo", self.browser.title)

		header = self.browser.find_element_by_tag_name('h1')
		self.assertIn('Login', header.text)

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('rob')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('CoffeeHouse')
		password_field.send_keys(Keys.RETURN)

		self.browser.get('%s%s' % (self.live_server_url, '/accounts/loggedin/'))
		continue_button = self.browser.find_element_by_tag_name('input').click()
		if continue_button:
			welcome_header = self.browser.find_element_by_tag_name('h2')
			self.assertIn('Welcome to LaserCo', welcome_header.text)

		self.browser.implicitly_wait(3)

	def test_add_engineer(self):
		""" Test that we can navigate from the front page and successfully add an engineer """

		# Maybe change this to navigation from home instead of using direct url?
		# ===================================================================================
		self.browser.get('%s%s' % (self.live_server_url, '/'))
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('rob')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('CoffeeHouse')
		password_field.send_keys(Keys.RETURN)

		self.browser.get('%s%s' % (self.live_server_url, '/accounts/loggedin/'))
		continue_button = self.browser.find_element_by_tag_name('input').click()
		if continue_button:

			print("We made it!")
			"""
			dropdown = self.browser.find_element_by_class_name("dropdown-toggle").click()
			engineer_button = self.browser.find_element_by_link_name('Engineer').click()

			first_name_field = self.browser.find_element_by_id('id_first_name')
			first_name_field.send_keys('Joey')
			last_name_field = self.browser.find_element_by_id('id_last_name')
			last_name_field.send_keys('Smith')
			last_name_field.send_keys(Keys.RETURN)
			"""
		print("We didn't make it.")

		self.browser.implicitly_wait(3)

	@skip("This is the big test, don't implement now")
	def test_serviceform(self):
		print("test_serviceform")
		self.browser.get('%s%s' % (self.live_server_url, '/'))

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('rob')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('CoffeeHouse')
		password_field.send_keys(Keys.RETURN)
		self.browser.get('%s%s' % (self.live_server_url, '/accounts/loggedin/'))
		continue_button = self.browser.find_element_by_tag_name('input').click()

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/serviceform/'))

		#engineer_field = Select(self.browser.find_element_by_id('id_info-engineer'))
		#engineer_field.select_by_value("1")
		all_options = self.browser.find_element_by_tag_name("select")
		for option in all_options:
			print(option)

		print("at SO form")
