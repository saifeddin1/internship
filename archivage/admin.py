from django.contrib import admin
from .models import Entreprise, Person, Formation, Marketing, Development
# Register your models here.

admin.site.register(Entreprise),
admin.site.register(Person),
admin.site.register(Formation),
admin.site.register(Marketing),
admin.site.register(Development),