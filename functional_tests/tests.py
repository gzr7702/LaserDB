from django.test import LiveServerTestCase
from unittest import skip
from datetime import date
import service_orders.tests.data as data
from service_orders.models import Machine, ServiceEngineer, Address, Customer, Part, ServiceLog

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

	@skip("not yet")
	def test_create_engineer(self):
		""" Test that we can successfully add an engineer """

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/engineerform/'))

		first_name_field = self.browser.find_element_by_id('id_first_name')
		first_name = "JoeyTest"
		first_name_field.send_keys(first_name)

		last_name_field = self.browser.find_element_by_id('id_last_name')
		last_name = "McTestGuy"
		last_name_field.send_keys(last_name)

		last_name_field.send_keys(Keys.RETURN)

		engineer = ServiceEngineer.objects.get(last_name=last_name)
		self.assertEqual(engineer.first_name, first_name, "First Names didn't match!")
		self.assertEqual(engineer.last_name, last_name, "Last names didn't match!")

		self.browser.implicitly_wait(3)

	@skip("for now")
	def test_create_customer(self):
		""" Test that we can successfully add a customer"""

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/customerform/'))

		company_name_field = self.browser.find_element_by_id('id_company_name')
		company_name = "Testing of Tests Inc."
		company_name_field.send_keys(company_name)

		contact_name_field = self.browser.find_element_by_id('id_contact_name')
		contact_name = "Billy Joe Test Guy"
		contact_name_field.send_keys(contact_name)

		email_field = self.browser.find_element_by_id('id_email')
		email = "TestGuy@testsinc.com"
		email_field.send_keys(email)

		email_field.send_keys(Keys.RETURN)


		customer = Customer.objects.get(company_name=company_name)
		self.assertEqual(customer.company_name, company_name, "Company Names didn't match!")
		self.assertEqual(customer.contact_name, contact_name, "Contact names didn't match!")
		self.assertEqual(customer.email, email, "Email addresses didn't match!")

		self.browser.implicitly_wait(3)

	@skip("not submitting to DB")
	def test_create_address(self):
		""" Test that we can successfully add an address"""

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/addressform/'))

		street_field = self.browser.find_element_by_id('id_street')
		street_address = "0001 Testing Boulevard"
		street_field.send_keys(street_address)

		city_field = self.browser.find_element_by_id('id_city')
		city = "Testville"
		city_field.send_keys(city)

		state_field = self.browser.find_element_by_id('id_state')
		state = "New Testico"
		state_field.send_keys(state)

		phone_field = self.browser.find_element_by_id('id_phone')
		phone_number = "212-555-1212"
		phone_field.send_keys(phone_number)

		phone_field.send_keys(Keys.RETURN)

		address = Address.objects.get(street=street_address)
		self.assertEqual(address.city, city, "City Names didn't match!")
		self.assertEqual(customer.state, state, "State names didn't match!")
		self.assertEqual(customer.phone, phone_number, "Phone numbers didn't match!")

		self.browser.implicitly_wait(3)

	def test_create_machine(self):
		""" Test that we can successfully add an address"""

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/machineform/'))

		serial_number_field = self.browser.find_element_by_id('id_serial_number')
		serial_number = "1000001"
		serial_number_field.send_keys(serial_number)

		model_field = self.browser.find_element_by_id('id_model')
		model = "The Tester"
		model_field.send_keys(model)

		manufacture_date_field = self.browser.find_element_by_id('id_manufacture_date')
		manufacture_date = date(2012, 3, 12)
		manufacture_date_field.send_keys(manufacture_date.strftime("%m/%d/%Y"))

		software_version_field = self.browser.find_element_by_id('id_software_version')
		software_version = "2.2.4"
		software_version_field.send_keys(software_version)

		passwd_field = self.browser.find_element_by_id('id_passwd')
		passwd = "Fido2112"
		passwd_field.send_keys(passwd)

		pulse_count_field = self.browser.find_element_by_id('id_pulse_count')
		pulse_count = "21212"
		pulse_count_field.send_keys(pulse_count)

		pulse_count_field.send_keys(Keys.RETURN)

		self.browser.implicitly_wait(3)

		#import pdb; pdb.set_trace()
		machine = Machine.objects.get(serial_number=serial_number)
		self.assertEqual(machine.model, model, "Models didn't match!")
		self.assertEqual(machine.manufacture_date, manufacture_date, "Manufacture dates didn't match!")
		self.assertEqual(machine.software_version, software_version, "Software versions didn't match!")
		self.assertEqual(machine.passwd, passwd, "Passwords didn't match!")


	@skip("This is the big test, don't implement now")
	def test_serviceform(self):

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/serviceform/'))

		all_options = self.browser.find_element_by_tag_name("select")
		for option in all_options:
			print(option)

		print("at SO form")
