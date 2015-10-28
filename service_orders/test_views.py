from django.test import TestCase, Client
from unittest import skip

class UnitTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.client.login(username='rob', password='CoffeeHouse')

	@skip("not yet")
	def test_add_engineer(self):
		#response = self.client.get('/partsinventory/individualreport/', {'rma_number': 234})
		response = self.client.post('/serviceorders/engineerform/', {'first_name': 'bilbo', 'last_name': 'baggins'})
		print(response.resolver_match.func)