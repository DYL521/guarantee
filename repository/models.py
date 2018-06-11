from django.db import models

# Create your models here.
'''
说是ForeignKey是one-to-many的，并举了一个车的例子：
有两个配件表，一个是车轮表，另一个是引擎表。两个表都有一个car字段，表示该配件对应的车。
对于车轮来说，多个对应一个car的情况很正常，所以car字段应该用ForeignKey来表示。
对于引擎来说，一个引擎只可能对应一个car，所以必须用OneToOneField。
OneToOneField(someModel) 可以理解为 ForeignKey(SomeModel, unique=True)。
　　
　　两者的反向查询是有差别的：
　　ForeignKey反向查询返回的是一个列表（一个车有多个轮子）。
　　OneToOneField反向查询返回的是一个模型示例（因为一对一关系）。
'''


class UserInfo(models.Model):
    '''
    用户表
    '''
    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)
    nickname = models.CharField(verbose_name='昵称', max_length=32)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    avatar = models.ImageField(verbose_name='头像')

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


class Blog(models.Model):
    '''博客信息'''
    nid = models.BigIntegerField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site = models.CharField(verbose_name='个人博客前缀', max_length=32, unique=True)
    theme = models.CharField(verbose_name='博客主题', max_length=32)

    ##  一对一， 一个博客对应一个用户
    user = models.OneToOneField(to='UserInfo', to_field='nid')


class UserFans(models.Model):
    '''
    互粉关系表
    '''
    user = models.ForeignKey(verbose_name='博主', to='UserInfo', to_field='nid', related_name='users')
    follower = models.ForeignKey(verbose_name='粉丝', to='UserInfo', to_field='nid', related_name='followers')

    class Meta:
        unique_together = [  ## 联合唯一
            ('user', 'follower')
        ]


class CateGory(models.Model):
    '''
    博主个人文章分类
    '''
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)

    blog = models.ForeignKey(verbose_name='所属博客', to='Blog', to_field='nid')


class ArticleDetail(models.Model):
    '''
     文章内容详细表
     content:内容
     artice: 关联文章id --一个文章只有一个主要内容
    '''
    content = models.TextField(verbose_name='文章内容')
    artice = models.OneToOneField(verbose_name='所属文章', to='Article', to_field='nid')


class UpDown(models.Model):
    '''
    文章踩或者是顶
    article ：踩或赞的文章--- 对应一篇文章
    user： 谁踩的、或者站---- 对应一个用户
    up：赞或者是踩
    '''

    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='nid')
    user = models.ForeignKey(verbose_name='赞或者踩的用户', to='UserInfo', to_field='nid')
    up = models.BooleanField(verbose_name='踩或者赞')




