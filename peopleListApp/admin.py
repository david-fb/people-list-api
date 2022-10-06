from django.contrib import admin
from .models.user import User
from .models.person import Person

# Register your models here.
admin.site.register(User)
admin.site.register(Person)