from django.contrib import admin
from .models import animal
from .models import protectora
from .models import Colaborador

# Register your models here.


admin.site.register(animal)
admin.site.register(Colaborador)
admin.site.register(protectora)