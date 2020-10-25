from django.db import models
import django.utils.timezone as timezone
# import mongoengine

# mongoengine.connect(host='mongodb://hsw:123@10.39.30.107:27017/testcase?authSource=admin&authMechanism=SCRAM-SHA-1')

class ApiTest(models.Model):
    brnum = models.CharField('BR号',max_length=10,null=True)
    #BR所属迭代
    brsprint = models.CharField('所属迭代',max_length=10,null=True)
    #案例描述
    tsdesc = models.CharField('案例描述',max_length=100,null=True)
    #所属产品
    tsppro = models.CharField('所属产品',max_length=10)
    #案例号
    tsnum = models.IntegerField('案例步骤')
    # 接口地址
    tsurl = models.CharField('接口地址', max_length=100)
    #请求方式
    tsrm = models.CharField('请求方式',max_length=8,null=True)
    #请求参数
    tspara = models.CharField('请求参数',max_length=500,null=True,blank=True)
    #请求头
    tsrh = models.CharField('接口请求头',max_length=100,null=True)
    #期待返回值
    tsexp = models.CharField('期待返回值',max_length=100,null=True)
    #录库时间
    tsdate = models.DateTimeField('录库时间',auto_now_add=True,editable=True)
    # tsdate.editable = True
    #RefererLink
    tsrefurl = models.CharField('Refere Link', max_length=300,null=True)
    isPass = models.BooleanField('是否通过',default=True)
    class Meta:
        unique_together=('brnum','tsurl')

# class ApiRunTab(models.Model)：

