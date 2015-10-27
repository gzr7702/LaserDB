from django.test import TestCase, Client, SimpleTestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from unittest import skip
from .views import home, auth_view


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

	def test_home_redirect(self):
		""" We test the redirect if user is not logged in """
		redirect_response = self.client.get('/', follow=True)
		self.assertRedirects(response=redirect_response, expected_url="/accounts/login/?next=/", status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	def test_home_view(self):
		""" Tests that we can access pages when logged in and that the proper
			template is used """
		success = self.client.login(username=self.user_id, password=self.user_password)
		self.assertEqual(success, True)
		response = self.client.get('/', follow=True)
		# We should not be redirected because we're logged in...
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

	def test_login_view(self):
		""" Test that the proper template was returned """
		response = self.client.get(reverse('login'))
		self.assertTemplateUsed(response, 'login.html')

	def test_auth_view_user_exists(self):
		""" Happy Path of auth_view() """
		request = self.factory.post(reverse('auth'), {'username': self.user_id, 'password': self.user_password})
		request.user = self.user_id
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = auth_view(request)
		self.assertEqual(response.url, '/accounts/loggedin/')

	def test_auth_view_user_no_exists(self):
		""" Sad Path of auth_view() """
		#import pdb; pdb.set_trace()	
		request = self.factory.post(reverse('auth'), {'username': 'syncopy', 'password': 'asdfasdf'})
		request.user = self.user_id
		request = add_middleware_to_request(request, SessionMiddleware)
		request.session.save()
		response = auth_view(request)
		self.assertEqual(response.url, '/accounts/invalid/')

	def test_loggedin_view(self):
		""" Test that the proper template was returned """
		response = self.client.get(reverse('loggedin'))
		self.assertTemplateUsed(response, 'loggedin.html')

	def test_invalid_login_view(self):
		""" Test that the proper template was returned """
		response = self.client.get(reverse('invalid_login'))
		self.assertTemplateUsed(response, 'invalid_login.html')

	def test_logout_view(self):
		""" Test that the proper template was returned """
		redirect_response = self.client.get(reverse('logout'), follow=True)
		self.assertRedirects(response=redirect_response, expected_url=reverse("login"), status_code=302, 
			target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

		self.assertTemplateUsed(redirect_response, 'login.html')
