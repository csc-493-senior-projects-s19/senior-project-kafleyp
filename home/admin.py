from django.contrib import admin
from .models import Food
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
	fields = ["food_title",
			  "food_time",
			  "food_content",
			  ]

	formfield_overrides = {

		models.TextField: {'widget': TinyMCE()}
	}




admin.site.register(Food, FoodAdmin)