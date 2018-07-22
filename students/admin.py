from django.contrib import admin

# Register your models here.
from .models import student
from .models import studentinstrument
from .models import instrument
from .models import instructor

admin.site.register(instrument)
admin.site.register(instructor)
admin.site.register(student)
admin.site.register(studentinstrument)
