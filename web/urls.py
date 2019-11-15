"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#导入了为项目和管理网站管理URL的函数和模块

urlpatterns = [
    #这个文件的主体定义了变量urlpatterns.
    #在这个针对整个项目的urls.py文件中，变量urlpatterns包含项目中的应用程序的URL
    path('admin/', admin.site.urls),
    #该处代码包含admin.site.urls，该模块定义了可在管理网站中请求的所有URL。
    path('',include('webs.urls',namespace='webs')),
    #此处我们添加了一行代码来包含模块webs.urls。这行代码包含实参namespace，
    #让我们能够将webs的URL同项目中的其他URL区分开来，这在项目开始扩展时很有帮助。
]
