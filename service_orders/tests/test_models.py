""" Tests for our models. Create is tested between setUP() and the read tests.
	Update and Delete have their own tests.
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from unittest import skip
from service_orders.models import Machine, ServiceEngineer, Address, Customer, Part, ServiceLog
import service_orders.tests.data as data
from datetime import date
from decimal import Decimal
from random import randint

class UnitTests(TestCase):
	def setUp(self):
		self.machine = Machine.objects.create(**data.machine_data)
		self.customer = Customer.objects.create(**data.customer_data)

		data.address_data['customer'] = self.customer
		self.address = Address.objects.create(**data.address_data)

		self.engineer = ServiceEngineer.objects.create(**data.engineer_name)

		data.service_order_data['customer'] = self.customer
		data.service_order_data['machine'] = self.machine
		data.service_order_data['engineer'] = self.engineer
		self.service_order = ServiceLog.objects.create(**data.service_order_data)

		data.part_data['service_log'] = self.service_order
		self.part = Part.objects.create(**data.part_data)

	def test_read_machine_data(self):
		retreived_machine = Machine.objects.get(serial_number=self.machine.serial_number)

		self.assertEqual(retreived_machine.model, data.machine_data['model'], "model didn't match!")
		self.assertEqual(retreived_machine.manufacture_date, data.machine_data['manufacture_date'], "manufacture_date didn't match!")
		self.assertEqual(retreived_machine.software_version, data.machine_data['software_version'], "software_version didn't match!")
		self.assertEqual(retreived_machine.passwd, data.machine_data['passwd'], "passwd didn't match!")
		self.assertEqual(retreived_machine.pulse_count, data.machine_data['pulse_count'], "pulse_count didn't match!")

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

	def test_delete_machine_data(self):
		serial_number = self.machine.serial_number
		self.machine.delete()

		with self.assertRaises(ObjectDoesNotExist):
			Machine.objects.get(serial_number=serial_number)

	def test_read_address_data(self):
		retreived_address = Address.objects.get(id=self.address.id)

		self.assertEqual(retreived_address.street, data.address_data['street'], "street didn't match!")
		self.assertEqual(retreived_address.city, data.address_data['city'], "city didn't match!")
		self.assertEqual(retreived_address.state, data.address_data['state'], "state didn't match!")
		self.assertEqual(retreived_address.zip_code, data.address_data['zip_code'], "zip didn't match!")
		self.assertEqual(retreived_address.phone, data.address_data['phone'], "phone_number didn't match!")
		self.assertEqual(retreived_address.address_type, data.address_data['address_type'], "address_type didn't match!")

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

	def test_delete_address_data(self):
		address_id = self.address.id
		self.address.delete()

		with self.assertRaises(ObjectDoesNotExist):
			Address.objects.get(id=address_id)

	def test_read_customer_data(self):
		retreived_customer = Customer.objects.get(id=self.customer.id)

		self.assertEqual(retreived_customer.company_name, data.customer_data['company_name'], "company_name didn't match!")
		self.assertEqual(retreived_customer.contact_name, data.customer_data['contact_name'], "contact_name didn't match!")
		self.assertEqual(retreived_customer.email, data.customer_data['email'], "email didn't match!")

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

	def test_delete_customer_data(self):
		customer_id = self.customer.id
		self.customer.delete()

		with self.assertRaises(ObjectDoesNotExist):
			Customer.objects.get(id=customer_id)

	def test_read_service_engineer_data(self):
		retreived_engineer = ServiceEngineer.objects.get(id=self.engineer.id)

		self.assertEqual(retreived_engineer.first_name, data.engineer_name['first_name'], "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, data.engineer_name['last_name'], "Last names didn't match!")

	def test_update_service_engineer_data(self):
		new_first_name = "Paula"
		self.engineer.first_name = new_first_name
		new_last_name = "Peduka"
		self.engineer.last_name = new_last_name
		self.engineer.save()

		retreived_engineer = ServiceEngineer.objects.get(id=self.engineer.id)

		self.assertEqual(retreived_engineer.first_name, new_first_name, "First Names didn't match!")
		self.assertEqual(retreived_engineer.last_name, new_last_name, "Last names didn't match!")

	def test_delete_service_engineer_data(self):
		service_engineer_id = self.engineer.id
		self.engineer.delete()

		with self.assertRaises(ObjectDoesNotExist):
			ServiceEngineer.objects.get(id=service_engineer_id)

	def test_read_part_data(self):
		""" We test all part data except for ServiceLog data since that would be redundant """
		retreived_part = Part.objects.get(serial_number=self.part.serial_number)

		self.assertEqual(retreived_part.serial_number, data.part_data['serial_number'], "serial_number didn't match!")
		self.assertEqual(retreived_part.part_number, data.part_data['part_number'], "part_number didn't match!")
		self.assertEqual(retreived_part.price, data.part_data['price'], "price didn't match!")
		self.assertEqual(retreived_part.location, data.part_data['location'], "location didn't match!")
		self.assertEqual(retreived_part.used, data.part_data['used'], "used didn't match!")

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

	def test_delete_part_data(self):
		serial_number = self.part.serial_number
		self.part.delete()

		with self.assertRaises(ObjectDoesNotExist):
			Part.objects.get(serial_number=serial_number)

	def test_read_service_order_data(self):
		retreived_service_log = ServiceLog.objects.get(rma_number=self.service_order.rma_number)

		self.assertEqual(retreived_service_log.rma_number, data.service_order_data['rma_number'], "rma_number didn't match!")
		self.assertEqual(retreived_service_log.date, data.service_order_data['date'], "date didn't match!")
		self.assertEqual(retreived_service_log.condition, data.service_order_data['condition'], "condition didn't match!")
		self.assertEqual(retreived_service_log.correction, data.service_order_data['correction'], "correction didn't match!")
		self.assertEqual(retreived_service_log.notes, data.service_order_data['notes'], "notes didn't match!")
		self.assertEqual(retreived_service_log.purchase_order, data.service_order_data['purchase_order'], "purchase_order didn't match!")
		self.assertEqual(retreived_service_log.zone_charge, data.service_order_data['zone_charge'], "zone_charge didn't match!")
		self.assertEqual(retreived_service_log.parts_charge, data.service_order_data['parts_charge'], "parts_charge didn't match!")
		self.assertEqual(retreived_service_log.customer, data.service_order_data['customer'], "customer didn't match!")
		self.assertEqual(retreived_service_log.machine, data.service_order_data['machine'], "machine didn't match!")
		self.assertEqual(retreived_service_log.engineer, data.service_order_data['engineer'], "engineer didn't match!")
		self.assertEqual(retreived_service_log.payment_category, data.service_order_data['payment_category'], "payment_category didn't match!")
		self.assertEqual(retreived_service_log.service_category, data.service_order_data['service_category'], "service_category didn't match!")

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

		self.assertEqual(retreived_service_log.date, new_date, "date didn't match!")
		self.assertEqual(retreived_service_log.condition, new_condition, "condition didn't match!")
		self.assertEqual(retreived_service_log.correction, new_correction, "correction didn't match!")
		self.assertEqual(retreived_service_log.notes, new_notes, "notes didn't match!")
		self.assertEqual(retreived_service_log.purchase_order, new_purchase_order, "purchase_order didn't match!")
		self.assertEqual(retreived_service_log.zone_charge, new_zone_charge, "zone_charge didn't match!")
		self.assertEqual(retreived_service_log.parts_charge, new_parts_charge, "parts_charge didn't match!")
		self.assertEqual(retreived_service_log.payment_category, new_payment_category, "payment_category didn't match!")
		self.assertEqual(retreived_service_log.service_category, new_service_category, "service_category didn't match!")

	def test_delete_service_order_data(self):
		rma_number = self.service_order.rma_number
		self.service_order.delete()

		with self.assertRaises(ObjectDoesNotExist):
			ServiceLog.objects.get(rma_number=rma_number)