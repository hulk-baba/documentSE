from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Documents(models.Model):
	Document = models.FileField(upload_to='uploads/', blank = False , null = False)
	keyword = models.CharField(max_length = 255)
	
	def __str__(self):
		return self.keyword



