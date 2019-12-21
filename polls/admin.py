from django.contrib import admin
from .models import Question
'''从polls.models引入Question'''
# Register your models here.
#向管理界面中加入投票应用
admin.site.register(Question)
