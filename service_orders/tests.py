from django.test import TestCase
from unittest import skip
from .models import Machine, ServiceEngineer, Address
from datetime import date

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

		self.engineer_name = {
			'first_name': 'Rob',
			'last_name': 'Smith'
		}

	def tearDown(self):
		pass

	@skip("skipping for now")
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

	@skip("skipping for now")
	def test_can_input_and_retrieve_service_engineer_data(self):
		ServiceEngineer.objects.create(**self.engineer_name)
		retreived_engineer = ServiceEngineer.objects.get(last_name=self.engineer_name['last_name'])

		self.assertEqual(retreived_engineer.first_name, self.engineer_name['first_name'], "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, self.engineer_name['last_name'], "Last names didn't match!")
