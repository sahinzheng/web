"""定义webs的URL模式（webs.urls）"""
#为了弄清当前位于哪个urls.py文件中，我们在这个文件开头添加了一个文档字符串。
from django.urls import path
#我们导入了函数path，因为我们需要使用它来将URL映射到视图。
from . import views
#我们导入了模块views，其中的句点让python从当前的urls.py模块所在的文件夹导入视图
app_name = 'webs'
urlpatterns = [
    #在这个模块中，变量urlpatterns是一个列表，包含可在应用程序webs中请求网页。
    #主页
    path('',views.index,name = 'index'),
    path('topics/',views.topics,name = 'topics'),
    #1、我们只是在用于主页URL的正则表达式中添加了topics/。
    #2、Django在检查请求的URL时，这个模式与这样的URL匹配：基础URL后面跟着topics。
    #3、可以在末尾包含斜杠，也可以省略它，但单词topics后面不能有任何东西，否则就与该模式不匹配。
    #4、其URL与该模式匹配的请求都将交给views.py中的函数topics()进行处理。
    path('topics/(?P<topic_id>\d+)/',views.topic,name='topic'),
]