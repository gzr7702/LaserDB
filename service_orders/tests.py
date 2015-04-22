from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SOTestCase(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_we_can_reach_front_page_and_login(self):
		self.browser.get('%s%s' % (self.live_server_url, '/'))
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
		print("Able to login")

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
		print("Able to login again")

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/serviceform/'))

		#engineer_field = Select(self.browser.find_element_by_id('id_info-engineer'))
		#engineer_field.select_by_value("1")
		all_options = self.browser.find_element_by_tag_name("select")
		for option in all_options:
			print(option)

		print("at SO form")

