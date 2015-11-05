from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.template.loader import render_to_string
from unittest import skip
from service_orders.views import home, individual_report, parts_home, parts_report
from service_orders.models import Machine, Customer, Address, ServiceEngineer, Part, ServiceLog
import service_orders.tests.data as data
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
		# Create dependant objects to service order
		data.service_order_data['customer'] = Customer.objects.create(**data.customer_data)
		data.service_order_data['machine'] = Machine.objects.create(**data.machine_data)
		data.service_order_data['engineer'] = ServiceEngineer.objects.create(**data.engineer_name)

		# Then create the service order itself and add it to the part data
		service_order = ServiceLog.objects.create(**data.service_order_data)	

		request = self.factory.get('individual_report/' + str(service_order.rma_number) + '/')
		request.user = self.user
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = individual_report(request, service_order.rma_number)
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
