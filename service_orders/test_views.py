from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from unittest import skip
from .views import home

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
		# Add models so we can test vars passed to template?
		self.assertTemplateUsed('service_orders.html', '/')
