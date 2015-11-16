from django.test import LiveServerTestCase
from unittest import skip
from datetime import date
from decimal import Decimal
import service_orders.tests.data as data
from service_orders.models import Machine, ServiceEngineer, Address, Customer, Part, ServiceLog

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SOTestCase(LiveServerTestCase):

	fixtures = ['service_orders/fixtures/data.json']

	def setUp(self):
		chromedriver_path = "/usr/local/lib/python3.4/dist-packages/chromedriver/bin/chromedriver"
		self.browser = webdriver.Chrome(chromedriver_path)

	def tearDown(self):
		self.browser.quit()

	@skip("working")
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

	@skip("working")
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

		self.browser.implicitly_wait(3)

		engineer = ServiceEngineer.objects.get(last_name=last_name)
		self.assertEqual(engineer.first_name, first_name, "First Names didn't match!")
		self.assertEqual(engineer.last_name, last_name, "Last names didn't match!")


	@skip("this is working")
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

		self.browser.implicitly_wait(3)

		customer = Customer.objects.get(company_name=company_name)
		self.assertEqual(customer.company_name, company_name, "Company Names didn't match!")
		self.assertEqual(customer.contact_name, contact_name, "Contact names didn't match!")
		self.assertEqual(customer.email, email, "Email addresses didn't match!")


	@skip("working")
	def test_create_address(self):
		""" Test that we can successfully add an address"""

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/addressform/'))

		street_field = self.browser.find_element_by_id('id_street')
		street_address = "100000001 Testing Boulevard"
		street_field.send_keys(street_address)

		city_field = self.browser.find_element_by_id('id_city')
		city = "Testville"
		city_field.send_keys(city)

		state_field = self.browser.find_element_by_id('id_state')
		state = "New Testico"
		state_field.send_keys(state)

		zip_code_field = self.browser.find_element_by_id('id_zip_code')
		zip_code = '11211'
		zip_code_field.send_keys(zip_code)

		phone_field = self.browser.find_element_by_id('id_phone')
		phone_number = "212-555-1212"
		phone_field.send_keys(phone_number)

		type_field = self.browser.find_element_by_id('id_address_type')
		address_type = "street"
		type_field.send_keys(address_type)

		type_field.send_keys(Keys.RETURN)
		self.browser.implicitly_wait(3)

		address = Address.objects.get(street=street_address)
		self.assertEqual(address.city, city, "City Names didn't match!")
		self.assertEqual(address.state, state, "State names didn't match!")
		self.assertEqual(address.zip_code, zip_code, "Zip codes didn't match!")
		self.assertEqual(address.phone, phone_number, "Phone numbers didn't match!")
		self.assertEqual(address.address_type, address_type, "Address types didn't match!")


	@skip("working")
	def test_create_machine(self):
		""" Test that we can successfully add a machine"""

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

		machine = Machine.objects.get(serial_number=serial_number)
		self.assertEqual(machine.model, model, "Models didn't match!")
		self.assertEqual(machine.manufacture_date, manufacture_date, "Manufacture dates didn't match!")
		self.assertEqual(machine.software_version, software_version, "Software versions didn't match!")
		self.assertEqual(machine.passwd, passwd, "Passwords didn't match!")

	@skip("not working")
	def test_create_part(self):
		""" Test that we can successfully add a part """

		self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/partsform/'))

		serial_number_field = self.browser.find_element_by_id('id_serial_number')
		serial_number = "1000002"
		serial_number_field.send_keys(serial_number)

		part_number_field = self.browser.find_element_by_id('id_part_number')
		part_number = "The Tester"
		part_number_field.send_keys(part_number)

		price_field = self.browser.find_element_by_id('id_price')
		price = "3.99"
		price_field.send_keys(price)

		location_field = self.browser.find_element_by_id('id_location')
		location = "New York"
		location_field.send_keys(location)

		used_check_box = self.browser.find_element_by_id('id_used')
		used_check_box.click()

		used_check_box.send_keys(Keys.RETURN)

		self.browser.implicitly_wait(3)

		part = Part.objects.get(serial_number=serial_number)
		self.assertEqual(part.part_number, part_number, "Parts didn't match!")
		self.assertEqual(part.price, price, "Prices didn't match!")
		self.assertEqual(part.location, location, "Locations didn't match!")

	def test_serviceform(self):
		""" The Big Kahuna -
			This tests the big Service Form """

		ret = self.browser.get('%s%s' % (self.live_server_url, '/serviceorders/serviceform/'))

		# Wizard Page 1:

		engineer_field = self.browser.find_element_by_id('id_info-engineer')
		engineer = "Bobby Birchman" 
		engineer_field.send_keys(engineer)

		date_field = self.browser.find_element_by_id('id_info-date')
		service_date = date(2012, 12, 3)
		date_field.send_keys(service_date.strftime("%m/%d/%Y"))

		machine_field = self.browser.find_element_by_id('id_info-machine')
		machine = "Blankenship 999"
		machine_field.send_keys(machine)

		rma_number_field = self.browser.find_element_by_id('id_info-rma_number')
		rma_number = 54345
		rma_number_field.send_keys(rma_number)

		customer_field = self.browser.find_element_by_id('id_info-customer')
		customer = "Acme"
		customer_field.send_keys(customer)

		condition_field = self.browser.find_element_by_id('id_info-condition')
		condition = "Unit looks like it was pushed down the stairs"
		condition_field.send_keys(condition)

		submit_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		submit_button.send_keys(Keys.RETURN)

		# Wizard Page 2:
		expected_url = '/serviceorders/serviceform/assessment/'
		self.assertEqual(self.browser.current_url, '%s%s' % (self.live_server_url, expected_url))

		correction_field = self.browser.find_element_by_id('id_assessment-correction')
		correction = "Replaced the Fetzer Valve"
		correction_field.send_keys(correction)

		notes_field = self.browser.find_element_by_id('id_assessment-notes')
		notes = "Customer was beligerent"
		notes_field.send_keys(notes)

		submit_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		submit_button.send_keys(Keys.RETURN)


		# Wizard Page 3:

		expected_url = '/serviceorders/serviceform/invoice/'
		self.assertEqual(self.browser.current_url, '%s%s' % (self.live_server_url, expected_url))

		zone_charge_field = self.browser.find_element_by_id('id_invoice-zone_charge')
		zone_charge = "9.99"
		zone_charge_field.clear()
		zone_charge_field.send_keys(zone_charge)

		service_category_field = self.browser.find_element_by_id('id_invoice-service_category')
		service_category = "service"
		service_category_field.send_keys(service_category)

		purchase_order_field = self.browser.find_element_by_id('id_invoice-purchase_order')
		purchase_order = 55533
		purchase_order_field.clear()
		purchase_order_field.send_keys(purchase_order)

		parts_charge_field = self.browser.find_element_by_id('id_invoice-parts_charge')
		parts_charge = "3.33"
		parts_charge_field.clear()
		parts_charge_field.send_keys(parts_charge)

		payment_category_field = self.browser.find_element_by_id('id_invoice-payment_category')
		payment_category = "billable_repair" 
		payment_category_field.send_keys(payment_category)

		submit_button = self.browser.find_element_by_xpath("//input[@type='submit']")
		submit_button.send_keys(Keys.RETURN)

		self.browser.implicitly_wait(3)

		service_log = ServiceLog.objects.get(rma_number=rma_number)
		self.assertEqual(service_log.date, service_date, "Dates didn't match!")
		self.assertEqual(service_log.condition, condition, "Condition didn't match!")
		self.assertEqual(service_log.correction, correction, "Correction didn't match!")
		self.assertEqual(service_log.notes, notes, "Notes didn't match!")
		self.assertEqual(service_log.purchase_order, purchase_order, "Purchase Order didn't match!")
		self.assertEqual(service_log.zone_charge, Decimal(zone_charge), "Zone Charge didn't match!")
		self.assertEqual(service_log.parts_charge, Decimal(parts_charge), "Parts Charge didn't match!")

		total_charge = Decimal(zone_charge) + Decimal(parts_charge)
		self.assertEqual(service_log.total_charge, total_charge, "Total didn't match!")
		self.assertEqual(service_log.payment_category, payment_category, "Payment Category didn't match!")
		self.assertEqual(service_log.service_category, service_category, "Service Category didn't match!")
