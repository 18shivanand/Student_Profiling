from django.contrib import admin
from .models import Experience, Education, Project, Skill


admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)