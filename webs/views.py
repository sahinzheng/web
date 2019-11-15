from django.shortcuts import render
from .models import Topic
#我们导入了与所需数据相关的模型。

# 在这里创建视图.

def index(request):
    """网站主页"""
    return render(request,'webs/index.html')

def topics(request):
#函数topics()包含一个形参：Django从服务器那里收到的request对象
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    #我们查询数据库——请求提供Topic对象，并按属性date_added对它们进行排序。我们将返回的查询集存储在topics中。
    context = {'topics':topics}
    #我们定义了一个将要发送给模板的上下文。
    #上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，
    #而值是我们要发送给模板的数据。
    #在这里只有一个键——值对，它包含我们将在网页中显示的一组主题。
    return render(request,'webs/topics.html',context)
    #创建使用数据的网页时，除对象request和模板的路径外，我们还将变量context传递给render().
    
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    #这是一个除request对象外还包含另一个形参的视图函数。
    #这个函数接受正则表达式（?P<topic_id>\d+）捕获的值，并将其存储到topic_id中。
    topic = Topic.objects.get(id=topic_id)
    #我们使用get()来获取指定的主题，就像前面在Django shell中所做的那样。
    entries = topic.entry_set.order_by('-date_added')
    #我们获取与该主题相关联的条目，并将它们按date_added排序：
    #date_added前面的减号指定按将序排列，即先显示最近的条目。
    context = {'topic':topic,'entries':entries}
    #我们将主题和条目都存储在字典context中。
    return render(request,'webs/topic.html',context)
    #再降这个字典发送给模板topic.html