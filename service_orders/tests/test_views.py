from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.loader import render_to_string
from unittest import skip
from service_orders.views import home, individual_report, parts_home, parts_report
from service_orders.models import Machine, Customer, Address, ServiceEngineer, Part, ServiceLog
from random import randint
from datetime import date
from decimal import Decimal

def add_middleware_to_request(request, middleware_class):
	""" Helper function for request factory """
	middleware = middleware_class()
	middleware.process_request(request)
	return request

def add_middleware_to_response(request, middleware_class):
	""" Helper function for request factory """
	middleware = middleware_class()
	middleware.process_request(request)
	return request


class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
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

	def test_home_view(self):
		request = self.factory.get(reverse('service_order_home'))
		request.user = self.user
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = home(request)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('service_orders.html'):
			render_to_string('service_orders.html')

	def test_individual_report_view(self):
		request = self.factory.get('individual_report/' + str(self.service_order.rma_number) + '/')
		request.user = self.user
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = individual_report(request, self.service_order.rma_number)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('individual_report.html'):
			render_to_string('individual_report.html')

	def test_parts_home_view(self):
		# what's the url?
		request = self.factory.get(reverse('parts'))
		request.user = self.user
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = parts_home(request)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('parts.html'):
			render_to_string('parts.html')

	@skip("")
	def test_parts_report_view(self):
		# what's the url?
		request = self.factory.get(reverse(''))
		request.user = self.user
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = parts_report(request, self.part.serial_number)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('parts_report.html'):
			render_to_string('parts_report.html')
