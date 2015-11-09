from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from unittest import skip
from service_orders.form_views import *
from service_orders.models import Customer, ServiceLog, ServiceEngineer, Machine, Part
from service_orders.forms import InfoForm, AssessmentForm, InvoiceForm
import service_orders.tests.data as data
from collections.abc import ValuesView
from collections import OrderedDict
from decimal import Decimal

class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()

	def test_post_engineer_form(self):
		response = self.client.post(reverse('engineer_form'), data.engineer_name)
		self.assertRedirects(response=response, expected_url=reverse('engineer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_engineer_form(self):
		response = self.client.get(reverse('engineer_form'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'engineerform.html')

	def test_post_customer_form(self):
		response = self.client.post(reverse('customer_form'), data.customer_data)
		self.assertRedirects(response=response, expected_url=reverse('customer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_customer_form(self):
		response = self.client.get(reverse('customer_form'))
		self.assertEqual(response.status_code, 200)
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
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'addressform.html')

	def test_post_machine_form(self):
		response = self.client.post(reverse('machine_form'), data.machine_data)
		self.assertRedirects(response=response, expected_url=reverse('machine_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_machine_form(self):
		response = self.client.get(reverse('machine_form'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'machineform.html')

	def test_post_parts_form(self):
		# Create dependant objects to service order
		data.service_order_data['customer'] = Customer.objects.create(**data.customer_data)
		data.service_order_data['machine'] = Machine.objects.create(**data.machine_data)
		data.service_order_data['engineer'] = ServiceEngineer.objects.create(**data.engineer_name)

		# Then create the service order itself and add it to the part data
		data.part_data['service_log'] = ServiceLog.objects.create(**data.service_order_data)

		response = self.client.post(reverse('parts_form'), data.part_data)
		self.assertRedirects(response=response, expected_url=reverse('parts_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_parts_form(self):
		response = self.client.get(reverse('parts_form'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'partsform.html')

	def test_add_parts_form_post(self):
		# Create dependant objects to service order
		data.service_order_data['customer'] = Customer.objects.create(**data.customer_data)
		data.service_order_data['machine'] = Machine.objects.create(**data.machine_data)
		data.service_order_data['engineer'] = ServiceEngineer.objects.create(**data.engineer_name)

		# Then create the service order itself and add it to the part data
		data.part_data['service_log'] = ServiceLog.objects.create(**data.service_order_data)
		response = self.client.post(reverse('add_parts_form'), data.part_data)
		self.assertRedirects(response=response, expected_url=reverse('add_parts_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_add_parts_form_get(self):
		response = self.client.get(reverse('add_parts_form'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'addpart.html')

	def test_process_form_data(self):
		# Create objects
		machine = Machine.objects.create(**data.machine_data)
		customer = Customer.objects.create(**data.customer_data)
		engineer = ServiceEngineer.objects.create(**data.engineer_name)

		# Create InfoForm
		info_form_data = {'engineer': engineer.id,
						'rma_number': data.service_order_data['rma_number'],
		 				'date': data.service_order_data['date'], 'customer': customer.id,
						'machine': machine.serial_number,
						'condition': data.service_order_data['condition']}
		info_form = InfoForm(info_form_data)

		# Create AssessmentForm
		assessment_form_data = {'correction': data.service_order_data['correction'],
								'notes': data.service_order_data['notes']}
		assessment_form = AssessmentForm(assessment_form_data)

		# Create InvoiceForm
		invoice_form_data = {'purchase_order': data.service_order_data['purchase_order'],
							'zone_charge': data.service_order_data['zone_charge'],
							'parts_charge': data.service_order_data['parts_charge'],
							'payment_category': data.service_order_data['payment_category'],
							'service_category': data.service_order_data['service_category']}
		invoice_form = InvoiceForm(invoice_form_data)

		form_list = ValuesView(OrderedDict([('info', info_form),
					('assessment', assessment_form), ('invoice', invoice_form)]))

		process_form_data(form_list)
		retreived_service_log = ServiceLog.objects.get(rma_number=data.service_order_data['rma_number'])

		# Yes, we are going to check each attr to make sure it was written to the DB
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

		# Most importantly, we'll check that the total is being calculated correctly
		total = Decimal('16.72')
		self.assertEqual(retreived_service_log.total_charge, total, "total didn't match!")

	def test_service_order_wizard(self):
		""" Test done(), but not get_template_names since it's part of Django """

		# Create objects
		machine = Machine.objects.create(**data.machine_data)
		customer = Customer.objects.create(**data.customer_data)
		engineer = ServiceEngineer.objects.create(**data.engineer_name)

		# Create InfoForm
		info_form_data = {'engineer': engineer.id,
						'rma_number': data.service_order_data['rma_number'],
		 				'date': data.service_order_data['date'], 'customer': customer.id,
						'machine': machine.serial_number,
						'condition': data.service_order_data['condition']}
		info_form = InfoForm(info_form_data)

		# Create AssessmentForm
		assessment_form_data = {'correction': data.service_order_data['correction'],
								'notes': data.service_order_data['notes']}
		assessment_form = AssessmentForm(assessment_form_data)

		# Create InvoiceForm
		invoice_form_data = {'purchase_order': data.service_order_data['purchase_order'],
							'zone_charge': data.service_order_data['zone_charge'],
							'parts_charge': data.service_order_data['parts_charge'],
							'payment_category': data.service_order_data['payment_category'],
							'service_category': data.service_order_data['service_category']}
		invoice_form = InvoiceForm(invoice_form_data)

		form_list = ValuesView(OrderedDict([('info', info_form),
					('assessment', assessment_form), ('invoice', invoice_form)]))

		sow = ServiceOrderWizard()
		response = sow.done(form_list)

		self.assertTemplateUsed(response, 'done.html')
