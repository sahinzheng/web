from django.db import models

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    #属性text是一个CharField--由字符或文本组成的数据，max_length=200为200个字符
    date_added = models.DateTimeField(auto_now_add=True)
    #属性date_added是一个DateTimeField--记录日期和时间的数据。
    #我们传递了实参auto_add_now=True，每当用户创建新主题时，这都让django将这个属性自动设置成当前日期和时间。
    #
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
        #我们需要告诉Django，默认使用哪个属性来显示有关主题的信息。Django调用方法__str__()来显示模型的简单表示。
        #在这里我们编写了方法__str__()，它返回存储在属性text中的字符串。


class Entry(models.Model):#像Topic一样，Entry也继承了Django基类Model。
    """学到的有关主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    #Topic是一个ForeignKey实例，
    text = models.TextField()
    #属性text是一个TextField实例。这种字段不需要长度限制，因为我们不想限制条目的长度
    date_added = models.DateTimeField(auto_now_add=True)
    #属性date_added让我们能够按创建顺序呈现条目，并在每个条目旁边防止时间戳
    
    class Meta:
        verbose_name_plural = 'entries'
        #我们在Entry类中嵌套了Meta类。Meta存储用于管理模型的额外信息，
        #在这里，它让我们能够设置一个特殊属性，
        #让Django在需要时使用Entries来表示多个条目。
        #如果没有这个类，Django将使用Entrys来表示多个条目。
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+'...'
    #方法__str__()告诉Django，呈现条目时显示哪些信息。
    #由于条目包含的文本可能很长，我们让Django只显示text的前50个字符。
    #我们还添加了一个省略号，指出显示的并非整个条目。
    
    
# Create your models here.
