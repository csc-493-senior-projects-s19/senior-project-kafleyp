from django.db import models
from datetime import datetime
# Create your models here.

class Food(models.Model):
	food_title = models.CharField(max_length = 200)
	food_content = models.TextField()
	food_time = models.DateTimeField("date published", default = datetime.now)

	def __str__(self):
		return self.food_title

