from django.contrib import admin
from webs.models import Topic,Entry#导入我们要注册的模型Topic,Entry
admin.site.register(Topic)#使用admin.site.register()让Django通过管理网站管理我们的模型。
admin.site.register(Entry)#使用admin.site.register()让Django通过管理网站管理我们的模型。

# Register your models here.
