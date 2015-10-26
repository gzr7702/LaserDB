from django.test import TestCase, Client, SimpleTestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from unittest import skip
from .views import home

class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user_id = 'rob'
		self.user_password = 'CoffeeHouse'
		self.user = User.objects.create_user(username='rob', password='CoffeeHouse')

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

	@skip('not yet')
	def test_auth_view(self):
		pass

	def test_loggedin_view(self):
		""" Test that the proper template was returned """
		response = self.client.get(reverse('loggedin'))
		self.assertTemplateUsed(response, 'loggedin.html')

	@skip("add variable test")
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
