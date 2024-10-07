from django.contrib import admin
from CV.models import competance,stage,formation,Type

class CompetanceAdmin(admin.ModelAdmin):
    list_display = ('comp', 'niveau')
    list_filter = ('comp', 'niveau')
    search_fields = ('comp', 'niveau')

class stageAdmin(admin.ModelAdmin):
    list_display = ('type', 'lieu')
    list_filter = ('type','lieu')
    date_hierarchy = 'date'
    search_fields = ('type', 'lieu')
class formationAdmin(admin.ModelAdmin):
    list_display = ('type', 'lieu','level')
    list_filter = ('type','lieu','level')
    search_fields = ('type', 'lieu','level')

admin.site.register(competance,CompetanceAdmin)
admin.site.register(stage,stageAdmin)
admin.site.register(formation)
admin.site.register(Type)



