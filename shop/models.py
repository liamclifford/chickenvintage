from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
import moneyed

class Listing(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
	key = models.SlugField(max_length=50)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
