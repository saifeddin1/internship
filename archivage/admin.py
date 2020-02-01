from django.contrib import admin
from .models import Entreprise, Person, Formation, Marketing, Development
# from django.contrib import messages 
# from .forms import AtLeastOneRequiredInlineFormSet

admin.site.register(Entreprise),
admin.site.register(Person),
admin.site.register(Formation),
admin.site.register(Marketing),
admin.site.register(Development),

# class FormationInline(admin.TabularInline):
#     model = Formation
#     formset = AtLeastOneRequiredInlineFormSet


# class ChairAdmin(admin.ModelAdmin):
#     inlines = [DeskInline,]

# admin.site.register(Chair, ChairAdmin)	