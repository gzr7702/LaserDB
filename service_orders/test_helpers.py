""" Helper functions for the test suite """

from .models import ServiceEngineer

def create_object(obj, object_data):
	#object_list = [k"=%s"%(k,v) for k, v in object_data.items()]
	object_list = []
	for k, v in object_data.items():
		object_list.append(k, v)
	print("object list ", object_list)
	# change to object ========================
	ServiceEngineer.objects.create(object_list)
