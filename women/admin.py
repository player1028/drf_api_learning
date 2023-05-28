from django.contrib import admin
from .models import Women, Category
# Register your models here.



@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'is_published']




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']