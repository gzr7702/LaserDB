from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.loader import render_to_string
from unittest import skip
from service_orders.form_views import engineer_form, customer_form
from service_orders.form_views import address_form, machine_form, parts_form
from service_orders.form_views import add_parts_form, process_form_data, ServiceOrderWizard
from random import randint
from datetime import date
from decimal import Decimal

class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user_id = 'rob'
		self.user_password = 'CoffeeHouse'
		self.user = User.objects.create_user(username=self.user_id, password=self.user_password)

		self.machine_data = {
			'serial_number': randint(500,10000),
	    	'model': 'The Bearfield',
	    	'manufacture_date': date(2014, 9, 20),
	    	'software_version': "2.25",
	    	'passwd': 'Frobnosticator',
	    	'pulse_count': 223
    	}

		self.customer_data = {
			'company_name': 'Mook Inc.',
	    	'contact_name': 'Joe Mook',
	    	'email': 'joe@joe.com',
    	}

		self.address_data = {
			'street': '1313 Mockingbird Ln.',
	    	'city': 'Los Angeles',
	    	'state': 'CA',
	    	'zip_code': 12345,
	    	'phone': '555-555-5555',
	    	'address_type': 'street'
    	}

		self.engineer_name = {
			'first_name': 'Rob',
			'last_name': 'Smith'
		}

		self.part_data = {
			'serial_number': randint(500, 10000),
			'part_number': 99999,
			'price': Decimal("9.99"),
			'location': 'Long Island',
			'used': True,
		}

		self.service_order_data = {
			'rma_number': randint(1, 800),
			'date': date(2015, 10, 13),
			'condition': 'It was broked',
			'correction': 'Fixeded it',
			'notes': 'This is customer has no idea how to treat an expensive laser.',
			'purchase_order': 66666,
			'zone_charge': Decimal("7.77"),
			'parts_charge': Decimal("8.95"),
			'payment_category': 'installation',
			'service_category': 'service',
		}

	def test_post_engineer_form(self):
		response = self.client.post(reverse('engineer_form'), self.engineer_name)
		self.assertRedirects(response=response, expected_url=reverse('engineer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_engineer_form(self):
		response = self.client.get(reverse('engineer_form'))
		self.assertTemplateUsed(response, 'engineerform.html')

	def test_post_customer_form(self):
		response = self.client.post(reverse('customer_form'), self.customer_data)
		self.assertRedirects(response=response, expected_url=reverse('customer_form'), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_get_customer_form(self):
		response = self.client.get(reverse('customer_form'))
		self.assertTemplateUsed(response, 'customerform.html')
