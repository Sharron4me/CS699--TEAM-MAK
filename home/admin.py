from django.contrib import admin
from .models import student, admintable, dish,waste, review, complaint,campaign

admin.site.register(student)
admin.site.register(admintable)
admin.site.register(dish)
admin.site.register(waste)
admin.site.register(review)
admin.site.register(complaint)
admin.site.register(campaign)
# Register your models here.
