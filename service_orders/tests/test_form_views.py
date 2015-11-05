from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from unittest import skip
from service_orders.form_views import *
from service_orders.models import Customer, ServiceLog, ServiceEngineer, Machine, Part
import service_orders.tests.data as data

class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()

	def test_post_engineer_form(self):
		response = self.client.post(reverse('engineer_form'), data.engineer_name)
		self.assertRedirects(response=response, expected_url=reverse('engineer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_engineer_form(self):
		response = self.client.get(reverse('engineer_form'))
		self.assertTemplateUsed(response, 'engineerform.html')

	def test_post_customer_form(self):
		response = self.client.post(reverse('customer_form'), data.customer_data)
		self.assertRedirects(response=response, expected_url=reverse('customer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_customer_form(self):
		response = self.client.get(reverse('customer_form'))
		self.assertTemplateUsed(response, 'customerform.html')

	def test_post_address_form(self):
		# Create a new customer object to be used in the address object
		new_customer = Customer.objects.create(**data.customer_data)
		data.address_data['customer'] = new_customer.id

		response = self.client.post(reverse('address_form'), data.address_data)
		self.assertRedirects(response=response, expected_url=reverse('address_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_address_form(self):
		response = self.client.get(reverse('address_form'))
		self.assertTemplateUsed(response, 'addressform.html')

	def test_post_machine_form(self):
		response = self.client.post(reverse('machine_form'), data.machine_data)
		self.assertRedirects(response=response, expected_url=reverse('machine_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_machine_form(self):
		response = self.client.get(reverse('machine_form'))
		self.assertTemplateUsed(response, 'machineform.html')

	@skip("data no good")
	def test_post_parts_form(self):
		# Create dependant objects to service order
		data.service_order_data['customer'] = Customer.objects.create(**data.customer_data)
		data.service_order_data['machine'] = Machine.objects.create(**data.machine_data)
		data.service_order_data['engineer'] = ServiceEngineer.objects.create(**data.engineer_name)

		# Then create the service order itself and add it to the part data
		data.part_data['service_orders'] = ServiceLog.objects.create(**data.service_order_data)

		response = self.client.post(reverse('parts_form'), data.part_data)
		self.assertRedirects(response=response, expected_url=reverse('parts_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_parts_form(self):
		response = self.client.get(reverse('parts_form'))
		self.assertTemplateUsed(response, 'partsform.html')

	@skip("not complete")
	def test_add_parts_form_post(self):
		response = self.client.post(reverse('add_parts_form'), data.part_data)
		self.assertRedirects(response=response, expected_url=reverse('add_parts_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_add_parts_form_get(self):
		response = self.client.get(reverse('add_parts_form'))
		self.assertTemplateUsed(response, 'addpart.html')

	@skip("not complete, need to add total")
	def test_process_form_data(self):
		pass
