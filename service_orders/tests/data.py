from random import randint
from datetime import date
from decimal import Decimal

machine_data = {
	'serial_number': randint(500,10000),
	'model': 'The Bearfield',
	'manufacture_date': date(2014, 9, 20),
	'software_version': "2.25",
	'passwd': 'Frobnosticator',
	'pulse_count': 223
}

customer_data = {
	'company_name': 'Mook Inc.',
	'contact_name': 'Joe Mook',
	'email': 'joe@joe.com',
}

address_data = {
	'street': '1313 Mockingbird Ln.',
	'city': 'Los Angeles',
	'state': 'CA',
	'zip_code': 12345,
	'phone': '555-555-5555',
	'address_type': 'street'
}

engineer_name = {
	'first_name': 'Rob',
	'last_name': 'Smith'
}

part_data = {
	'serial_number': randint(500, 10000),
	'part_number': 99999,
	'price': Decimal("9.99"),
	'location': 'Long Island',
	'used': True,
}

service_order_data = {
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
