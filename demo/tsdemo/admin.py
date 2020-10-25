from django.contrib import admin

# Register your models here.
from .models import ApiTest
@admin.register(ApiTest)
class ApiTestAdmin(admin.ModelAdmin):
    def necenum(self):
        return self.brnum
    necenum.short_description = "BR号"
    def sprintnum(self):
        return self.brsprint
    sprintnum.short_description = '所属迭代'
    def requestmethod(self):
        return self.tsrm
    requestmethod.short_description = '请求方式'
    def tsdescrip(self):
        return self.tsdesc
    tsdescrip.short_description = "案例描述"
    def status(self):
        if self.isPass:
            return "通过"
        else:
            return "失败"
    status.short_description = "执行结果"
    def number(self):
        return self.tsnum
    number.short_description = "测试案例编号"
    def extime(self):
        return self.tsdate
    extime.short_description = "录库时间"
    def url(self):
        return self.tsurl
    url.short_description = "接口地址"
    def proname(self):
        return self.tsppro
    proname.short_description = "所属产品"
    def requestheader(self):
        return self.tsrh
    requestheader.short_description = "请求头"
    def requestparamer(self):
        return self.tspara
    requestparamer.short_description = "请求参数"
    def tsexpected(self):
        return self.tsexp
    tsexpected.short_description = "期待返回值"
    def tsreferlink(self):
        return self.tsrefurl
    tsreferlink.short_description = "Refer Link"
    #显示字段
    list_display = [necenum,sprintnum,proname,tsdescrip,number,extime,url,requestmethod,requestparamer,requestheader,tsreferlink,status]
    #过滤字段
    list_filter = ['tsnum','tsppro','isPass']
    #搜索字段
    search_fields = ['brsprint','tsnum','tsdesc','tsurl']
    #分页，每页条目数为10
    list_per_page = 10
    #规定属性顺序
    # fields = (('brnum','tsnum'),'tsppro','tsurl')
    #属性分组
    fieldsets = [
        ("基础信息",{"fields":['brnum','brsprint','tsnum','tsppro','tsdesc']}),
        ("接口测试",{"fields":['tsurl','tsrefurl','tsrm','tspara','tsrh','tsexp']})
    ]

# admin.site.register(TestPro,TestProAdmin)
# admin.register(TestPro)
