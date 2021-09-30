import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_aero.settings")
import django
django.setup()
import json

from main.models import Interface

def main():
	"""Загрузить информацию в бд из файла init_data/test.json"""
	with open("init_data/test.json") as file:
		data = json.load(file)
	for item in data:
		interface = Interface.objects.update_or_create(ifindex = item.get("ifindex"), 
			defaults = {"ifname":item.get("ifname"), "mtu":item.get("mtu"), "operstate":item.get("operstate"),
			"mac_address":item.get("mac_address"), "ip":item.get("ip")})

if __name__ == '__main__':
	main()