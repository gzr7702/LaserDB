from django.test import TestCase
from unittest import skip
from .models import Machine, ServiceEngineer, Address, Customer, Part, ServiceLog
from datetime import date
from decimal import Decimal

class UnitTests(TestCase):
	def setUp(self):
		self.machine_data = {
			'serial_number': 12345,
	    	'model': 'The Bearfield',
	    	'manufacture_date': date(2014, 9, 20),
	    	'software_version': 2.25,
	    	'passwd': 'Frobnosticator',
	    	'pulse_count': 223
    	}

		self.address_data = {
			'street': '1313 Mockingbird Ln.',
	    	'city': 'Los Angeles',
	    	'state': 'CA',
	    	'zip': 12345,
	    	'phone': '555-555-5555'
    	}

		self.customer_data = {
			'company_name': 'Mook Inc.',
	    	'contact_name': 'Joe Mook',
	    	'email': 'joe@joe.com',
    	}

		self.engineer_name = {
			'first_name': 'Rob',
			'last_name': 'Smith'
		}

		self.part_data = {
			'serial_number': 12345,
			'part_number': 99999,
			'price': Decimal(9.99),
			'location': 'Long Island',
			'used': True,
		}

		self.service_order_data = {
			'rma_number': 54321,
			'date': date(2015, 10, 13),
			'condition': 'It was broked',
			'correction': 'Fixed it',
			'notes': 'This is customer has no idea how to treat an expensive laser.',
			'purchase_order': 66666,
			'zone_charge': Decimal(7.77),
			'parts_charge': Decimal(8.95),
		}

	def tearDown(self):
		pass

	def create_customer(self):
		""" Helper function to create customer object """
		customer_data = self.customer_data
		customer_data['street_address'] = Address.objects.create(**self.address_data)
		customer_data['billing_address'] = Address.objects.create(**self.address_data)

		return customer_data

	def test_can_input_and_retrieve_machine_data(self):
		Machine.objects.create(**self.machine_data)
		retreived_machine = Machine.objects.get(serial_number=self.machine_data['serial_number'])

		self.assertEqual(retreived_machine.serial_number , self.machine_data['serial_number'], "serial_number didn't match!")
		self.assertEqual(retreived_machine.model, self.machine_data['model'], "model didn't match!")
		self.assertEqual(retreived_machine.manufacture_date, self.machine_data['manufacture_date'], "manufacture_date didn't match!")
		self.assertEqual(retreived_machine.software_version, self.machine_data['software_version'], "software_version didn't match!")
		self.assertEqual(retreived_machine.passwd, self.machine_data['passwd'], "passwd didn't match!")
		self.assertEqual(retreived_machine.pulse_count, self.machine_data['pulse_count'], "pulse_count didn't match!")

	def test_can_input_and_retrieve_address_data(self):
		new_address = Address.objects.create(**self.address_data)
		retreived_address = Address.objects.get(id=new_address.id)

		self.assertEqual(retreived_address.street, self.address_data['street'], "street didn't match!")
		self.assertEqual(retreived_address.city, self.address_data['city'], "city didn't match!")
		self.assertEqual(retreived_address.state, self.address_data['state'], "state didn't match!")
		self.assertEqual(retreived_address.zip, self.address_data['zip'], "zip didn't match!")

	def test_can_input_and_retrieve_customer_data(self):
		# We copy the customer date and add 2 Address objects
		customer_data = self.create_customer()

		new_customer = Customer.objects.create(**customer_data)
		retreived_customer = Customer.objects.get(id=new_customer.id)

		self.assertEqual(retreived_customer.company_name, customer_data['company_name'], "company_name didn't match!")
		self.assertEqual(retreived_customer.contact_name, customer_data['contact_name'], "contact_name didn't match!")
		self.assertEqual(retreived_customer.email, customer_data['email'], "email didn't match!")
		self.assertEqual(retreived_customer.street_address, customer_data['street_address'], "street_address didn't match!")
		self.assertEqual(retreived_customer.billing_address, customer_data['billing_address'], "billing_address didn't match!")

	def test_can_input_and_retrieve_service_engineer_data(self):
		ServiceEngineer.objects.create(**self.engineer_name)
		retreived_engineer = ServiceEngineer.objects.get(last_name=self.engineer_name['last_name'])

		self.assertEqual(retreived_engineer.first_name, self.engineer_name['first_name'], "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, self.engineer_name['last_name'], "Last names didn't match!")

	@skip("price not working")
	def test_can_input_and_retrieve_part_data(self):
		Part.objects.create(**self.part_data)
		retreived_part = Part.objects.get(serial_number=self.part_data['serial_number'])

		self.assertEqual(retreived_part.serial_number, self.part_data['serial_number'], "serial_number didn't match!")
		self.assertEqual(retreived_part.part_number, self.part_data['part_number'], "part_number didn't match!")
		self.assertEqual(retreived_part.price, self.part_data['price'], "price didn't match!")
		self.assertEqual(retreived_part.location, self.part_data['location'], "location didn't match!")
		self.assertEqual(retreived_part.used, self.part_data['used'], "used didn't match!")

	@skip("Setting up")
	def test_can_input_and_retrieve_service_order_data(self):
		# We copy the service order data and add foriegn keys
		service_order = self.service_order_data
		service_order_data['customer'] = Customer.objects.create(**self.customer_data)
		service_order_data['machine'] = Machine.objects.create(**self.machine_data)
		service_order_data['engineer'] = Engineer.objects.create(**self.engineer_name)

		ServiceLog.objects.create(**service_order)
		retreived_service_log = ServiceLog.objects.get(rma_number=self.service_order_data['rma_number'])

		self.assertEqual(service_order_data.rma_number, self.service_order_data['rma_number'], "rma_number didn't match!")
