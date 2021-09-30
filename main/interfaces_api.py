from .models import Interface
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError

def get_interfaces():
	"""Возвращает информацию о всех интерфейсах в формате dict"""
	interfaces = Interface.objects.all()
	result = [{
		"ifindex" : interface.ifindex,
		"ifname" : interface.ifname,
		"mtu" : interface.mtu,
		"operstate" : interface.operstate,
		"mac_address" : interface.mac_address,
		"ip" : interface.ip if interface.ip else ""
		} for interface in interfaces] 

	return result

def change_ips(data):
	"""Изменяет ip адресса принимает список из словарей с полями id и ip"""
	result = {"status":"ok"}
	for item in data:
		ifindex = int(item["id"])
		ip = item["ip"]
		interface = Interface.objects.filter(ifindex = ifindex)[0]
		if ip != "":
			try:
				validate_ipv46_address(ip)
			except ValidationError:
				result["status"] = "err"
				if "errors" not in result:
					result["errors"] = []
				result["errors"].append({"message":f"{ip} is bad value for ip", "id": ifindex, "ip": ip})
				continue
		interface.ip = ip
		interface.save()
	return result