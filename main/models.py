from django.db import models

# Create your models here.

class Interface(models.Model):
	ifindex = models.IntegerField(unique=True)
	ifname = models.CharField(max_length=256, blank=True)
	mtu = models.IntegerField()
	operstate = models.CharField(max_length=256, blank=True)
	mac_address = models.CharField(max_length=256, blank=True)
	ip = models.GenericIPAddressField(null = True, blank=True)
	def __str__(self):
		ip_str = "with ip " + str(self.ip) if self.ip else "without ip"
		return f"({self.ifindex}) {self.ifname} interface {ip_str}"