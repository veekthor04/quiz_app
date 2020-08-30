from django.contrib import admin
from .models import Passage, Question, SiteConfiguration    
from solo.admin import SingletonModelAdmin

# Register your models here.
class PassageAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Passage, PassageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(SiteConfiguration, SingletonModelAdmin)