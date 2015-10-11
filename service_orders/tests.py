from django.test import TestCase
from unittest import skip
from .models import Machine, ServiceEngineer
from datetime import date

class UnitTests(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_can_input_and_retrieve_machine_data(self):
		machine_data = {
			'serial_number': 12345,
	    	'model': "The Bearfield",
	    	'manufacture_date': date(2014, 9, 20),
	    	'software_version': 2.25,
	    	'passwd': "Frobnosticator",
	    	'pulse_count': 223
    	}

		Machine.objects.create(**machine_data)
		retreived_machine = Machine.objects.get(serial_number=machine_data['serial_number'])
		
		self.assertEqual(retreived_machine.serial_number, machine_data['serial_number'], "Searial numbers didn't match!")


	#@skip("skipping for now")
	def test_can_input_and_retrieve_service_engineer_data(self):
		name = {
			'first_name': 'Rob',
			'last_name': 'Smith'
		}

		ServiceEngineer.objects.create(**name)
		retreived_engineer = ServiceEngineer.objects.get(last_name=name['last_name'])

		self.assertEqual(retreived_engineer.first_name, name['first_name'], "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, name['last_name'], "Last names didn't match!")
