from django.contrib import admin

from .models import Question, Choice
# Register your models here.
# Credits - please note this code is sourced from the 
# Official Django documentation on poll tutorials and
# is fully acknowledged & accredited in readme

admin.site.register(Question)
admin.site.register(Choice)
