""" Tests for our models. Create is tested between setUP() and the read tests.
	Update and Delete have their own tests.
"""

from django.test import TestCase
from unittest import skip
from .models import Machine, ServiceEngineer, Address, Customer, Part, ServiceLog
from datetime import date
from decimal import Decimal
from random import randint

class UnitTests(TestCase):
	def setUp(self):
		self.machine_data = {
			'serial_number': randint(500,10000),
	    	'model': 'The Bearfield',
	    	'manufacture_date': date(2014, 9, 20),
	    	'software_version': "2.25",
	    	'passwd': 'Frobnosticator',
	    	'pulse_count': 223
    	}
		self.machine = Machine.objects.create(**self.machine_data)

		self.customer_data = {
			'company_name': 'Mook Inc.',
	    	'contact_name': 'Joe Mook',
	    	'email': 'joe@joe.com',
    	}
		self.customer = Customer.objects.create(**self.customer_data)

		self.address_data = {
			'street': '1313 Mockingbird Ln.',
	    	'city': 'Los Angeles',
	    	'state': 'CA',
	    	'zip_code': 12345,
	    	'phone': '555-555-5555',
			'customer': Customer.objects.create(**self.customer_data),
	    	'address_type': 'street'
    	}
		self.address = Address.objects.create(**self.address_data)

		self.engineer_name = {
			'first_name': 'Rob',
			'last_name': 'Smith'
		}
		self.engineer = ServiceEngineer.objects.create(**self.engineer_name)

		self.part_data = {
			'serial_number': randint(500, 10000),
			'part_number': 99999,
			'price': Decimal("9.99"),
			'location': 'Long Island',
			'used': True,
		}
		self.part = Part.objects.create(**self.part_data)

		self.service_order_data = {
			'rma_number': randint(1, 800),
			'customer': Customer.objects.create(**self.customer_data),
			'machine': self.machine,
			'date': date(2015, 10, 13),
			'condition': 'It was broked',
			'correction': 'Fixeded it',
			'notes': 'This is customer has no idea how to treat an expensive laser.',
			'engineer': ServiceEngineer.objects.create(**self.engineer_name),
			'purchase_order': 66666,
			'zone_charge': Decimal("7.77"),
			'parts_charge': Decimal("8.95"),
			'payment_category': 'installation',
			'service_category': 'service',
		}
		self.service_order = ServiceLog.objects.create(**self.service_order_data)

	def test_read_machine_data(self):
		retreived_machine = Machine.objects.get(serial_number=self.machine_data['serial_number'])

		self.assertEqual(retreived_machine.serial_number , self.machine_data['serial_number'], "serial_number didn't match!")
		self.assertEqual(retreived_machine.model, self.machine_data['model'], "model didn't match!")
		self.assertEqual(retreived_machine.manufacture_date, self.machine_data['manufacture_date'], "manufacture_date didn't match!")
		self.assertEqual(retreived_machine.software_version, self.machine_data['software_version'], "software_version didn't match!")
		self.assertEqual(retreived_machine.passwd, self.machine_data['passwd'], "passwd didn't match!")
		self.assertEqual(retreived_machine.pulse_count, self.machine_data['pulse_count'], "pulse_count didn't match!")

	def test_update_machine_data(self):
		new_model = "Smithfield 7"
		self.machine.model = new_model
		new_date = date(2015, 10, 20)
		self.machine.manufacture_date = new_date
		new_software_version = "5.9.88"
		self.machine.software_version = new_software_version
		new_password = "nadafinga"
		self.machine.passwd= new_password
		new_pulse_count = 440
		self.machine.pulse_count = new_pulse_count

		self.machine.save()
		retreived_machine = Machine.objects.get(serial_number=self.machine.serial_number)

		self.assertEqual(retreived_machine.model, new_model, "serial_number didn't match!")
		self.assertEqual(retreived_machine.manufacture_date, new_date, "manufacture_date didn't match!")
		self.assertEqual(retreived_machine.software_version, new_software_version, "software_version didn't match!")
		self.assertEqual(retreived_machine.passwd, new_password, "passwd didn't match!")
		self.assertEqual(retreived_machine.pulse_count, new_pulse_count, "pulse_count didn't match!")

	def test_read_address_data(self):
		retreived_address = Address.objects.get(id=self.address.id)

		self.assertEqual(retreived_address.street, self.address_data['street'], "street didn't match!")
		self.assertEqual(retreived_address.city, self.address_data['city'], "city didn't match!")
		self.assertEqual(retreived_address.state, self.address_data['state'], "state didn't match!")
		self.assertEqual(retreived_address.zip_code, self.address_data['zip_code'], "zip didn't match!")
		self.assertEqual(retreived_address.phone, self.address_data['phone'], "phone_number didn't match!")
		self.assertEqual(retreived_address.address_type, self.address_data['address_type'], "address_type didn't match!")

	def test_update_address_data(self):
		new_street = "44 Main Street"
		self.address.street = new_street
		new_city = "Piscataway"
		self.address.city = new_city
		new_state = "Joisey"
		self.address.state = new_state
		new_zip = 76543
		self.address.zip_code = new_zip
		new_phone_number = "212-222-2222"
		self.address.phone = new_phone_number
		new_address_type = "billing"
		self.address.address_type = new_address_type

		self.address.save()
		retreived_address = Address.objects.get(id=self.address.id)

		self.assertEqual(retreived_address.street, new_street, "street didn't match!")
		self.assertEqual(retreived_address.city, new_city, "city didn't match!")
		self.assertEqual(retreived_address.state, new_state, "state didn't match!")
		self.assertEqual(retreived_address.zip_code, new_zip, "zip didn't match!")
		self.assertEqual(retreived_address.phone, new_phone_number, "phone_number didn't match!")
		self.assertEqual(retreived_address.address_type, new_address_type, "address_type didn't match!")

	def test_read_customer_data(self):
		retreived_customer = Customer.objects.get(id=self.customer.id)

		self.assertEqual(retreived_customer.company_name, self.customer_data['company_name'], "company_name didn't match!")
		self.assertEqual(retreived_customer.contact_name, self.customer_data['contact_name'], "contact_name didn't match!")
		self.assertEqual(retreived_customer.email, self.customer_data['email'], "email didn't match!")

	def test_update_customer_data(self):
		new_company_name = "Bobby's Laser House"
		self.customer.company_name = new_company_name
		new_contact_name = "Bobby Benuccio"
		self.customer.contact_name = new_contact_name
		new_email = "bobby@blh.com"
		self.customer.email = new_email

		self.customer.save()
		retreived_customer = Customer.objects.get(id=self.customer.id)

		self.assertEqual(retreived_customer.company_name, new_company_name, "company_name didn't match!")
		self.assertEqual(retreived_customer.contact_name, new_contact_name, "contact_name didn't match!")
		self.assertEqual(retreived_customer.email, new_email, "email didn't match!")

	def test_read_service_engineer_data(self):
		retreived_engineer = ServiceEngineer.objects.get(id=self.engineer.id)

		self.assertEqual(retreived_engineer.first_name, self.engineer_name['first_name'], "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, self.engineer_name['last_name'], "Last names didn't match!")

	def test_update_service_engineer_data(self):
		new_first_name = "Paula"
		self.engineer.first_name = new_first_name
		new_last_name = "Peduka"
		self.engineer.last_name = new_last_name
		self.engineer.save()

		retreived_engineer = ServiceEngineer.objects.get(id=self.engineer.id)

		self.assertEqual(retreived_engineer.first_name, new_first_name, "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, new_last_name, "Last names didn't match!")

	def test_read_part_data(self):
		""" We test all part data except for ServiceLog data since that would be redundant """
		retreived_part = Part.objects.get(serial_number=self.part.serial_number)

		self.assertEqual(retreived_part.serial_number, self.part_data['serial_number'], "serial_number didn't match!")
		self.assertEqual(retreived_part.part_number, self.part_data['part_number'], "part_number didn't match!")
		self.assertEqual(retreived_part.price, self.part_data['price'], "price didn't match!")
		self.assertEqual(retreived_part.location, self.part_data['location'], "location didn't match!")
		self.assertEqual(retreived_part.used, self.part_data['used'], "used didn't match!")

	def test_update_part_data(self):
		""" We test all part data except for ServiceLog data since that would be redundant """
		new_part_number = 7777
		self.part.part_number = new_part_number
		new_price = Decimal("4.95")
		self.part.price = new_price
		new_location = "Mattapan"
		self.part.location = new_location
		new_used = False
		self.part.used = new_used
		self.part.save()

		retreived_part = Part.objects.get(serial_number=self.part.serial_number)

		self.assertEqual(retreived_part.part_number, new_part_number, "part_number didn't match!")
		self.assertEqual(retreived_part.price, new_price, "price didn't match!")
		self.assertEqual(retreived_part.location, new_location, "location didn't match!")
		self.assertEqual(retreived_part.used, new_used, "used didn't match!")

	def test_read_service_order_data(self):
		retreived_service_log = ServiceLog.objects.get(rma_number=self.service_order.rma_number)

		self.assertEqual(retreived_service_log.rma_number, self.service_order.rma_number, "rma_number didn't match!")
		self.assertEqual(retreived_service_log.date, self.service_order.date, "date didn't match!")
		self.assertEqual(retreived_service_log.condition, self.service_order.condition, "condition didn't match!")
		self.assertEqual(retreived_service_log.correction, self.service_order.correction, "correction didn't match!")
		self.assertEqual(retreived_service_log.notes, self.service_order.notes, "notes didn't match!")
		self.assertEqual(retreived_service_log.purchase_order, self.service_order.purchase_order, "purchase_order didn't match!")
		self.assertEqual(retreived_service_log.zone_charge, self.service_order.zone_charge, "zone_charge didn't match!")
		self.assertEqual(retreived_service_log.parts_charge, self.service_order.parts_charge, "parts_charge didn't match!")
		self.assertEqual(retreived_service_log.customer, self.service_order.customer, "customer didn't match!")
		self.assertEqual(retreived_service_log.machine, self.service_order.machine, "machine didn't match!")
		self.assertEqual(retreived_service_log.engineer, self.service_order.engineer, "engineer didn't match!")
		self.assertEqual(retreived_service_log.payment_category, self.service_order.payment_category, "payment_category didn't match!")
		self.assertEqual(retreived_service_log.service_category, self.service_order.service_category, "service_category didn't match!")

	def test_update_service_order_data(self):
		new_date = date(2013, 4, 22)
		self.service_order.date = new_date
		new_condition = 'It was thrown down the stairs'
		self.service_order.condition = new_condition
		new_correction = 'Replaced mirror'
		self.service_order.correction = new_correction
		new_notes = 'They broke 0sdfasdfasdfthe mirror'
		self.service_order.notes = new_notes
		new_purchase_order = 8888
		self.service_order.purchase_order = new_purchase_order
		new_zone_charge = Decimal("2.30")
		self.service_order.zone_charge = new_zone_charge
		new_parts_charge= Decimal("3.44")
		self.service_order.parts_charge = new_parts_charge
		new_payment_category= 'sales_mkt_dem'
		self.service_order.payment_category = new_payment_category
		new_service_category= 'complaint'
		self.service_order.service_category = new_service_category

		self.service_order.save()

		retreived_service_log = ServiceLog.objects.get(rma_number=self.service_order.rma_number)

		self.assertEqual(retreived_service_log.rma_number, self.service_order.rma_number, "rma_number didn't match!")
		self.assertEqual(retreived_service_log.date, self.service_order.date, "date didn't match!")
		self.assertEqual(retreived_service_log.condition, self.service_order.condition, "condition didn't match!")
		self.assertEqual(retreived_service_log.correction, self.service_order.correction, "correction didn't match!")
		self.assertEqual(retreived_service_log.notes, self.service_order.notes, "notes didn't match!")
		self.assertEqual(retreived_service_log.purchase_order, self.service_order.purchase_order, "purchase_order didn't match!")
		self.assertEqual(retreived_service_log.zone_charge, self.service_order.zone_charge, "zone_charge didn't match!")
		self.assertEqual(retreived_service_log.parts_charge, self.service_order.parts_charge, "parts_charge didn't match!")
		self.assertEqual(retreived_service_log.customer, self.service_order.customer, "customer didn't match!")
		self.assertEqual(retreived_service_log.machine, self.service_order.machine, "machine didn't match!")
		self.assertEqual(retreived_service_log.engineer, self.service_order.engineer, "engineer didn't match!")
		self.assertEqual(retreived_service_log.payment_category, self.service_order.payment_category, "payment_category didn't match!")
		self.assertEqual(retreived_service_log.service_category, self.service_order.service_category, "service_category didn't match!")
